"""
sentry_bitbucket.plugin
~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013 by Atomised Co-operative Ltd.
:license: BSD, see LICENSE for more details.
"""
import requests
import sentry_bitbucket

from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from sentry.plugins.bases.issue import IssuePlugin

from requests_oauthlib import OAuth1


class BitbucketOptionsForm(forms.Form):
    repo = forms.CharField(label=_('Repository Name'),
        widget=forms.TextInput(attrs={'class': 'span3', 'placeholder': 'e.g. getsentry/sentry'}),
        help_text=_('Enter your repository name, including the owner.'))


class BitbucketIssueForm(forms.Form):
    ISSUE_TYPES = (
        ('bug', 'Bug'),
        ('enhancement', 'Enhancement'),
        ('proposal', 'Proposal'),
        ('task', 'Task'),
    )
    PRIORITIES = (
        ('trivial', 'Trivial',),
        ('minor', 'Minor',),
        ('major', 'Major'),
        ('critical', 'Critical'),
        ('blocker', 'Blocker'),
    )

    title = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'span9'}),
                            required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'span9'}),
                                    required=True)
    issue_type = forms.ChoiceField(choices=ISSUE_TYPES)
    priority = forms.ChoiceField(choices=PRIORITIES)


class BitbucketPlugin(IssuePlugin):
    new_issue_form = BitbucketIssueForm
    author = 'Neil Albrock'
    author_url = 'http://atomised.coop'
    version = sentry_bitbucket.VERSION
    description = "Integrate Bitbucket issues by linking a repository to a project."
    resource_links = [
        ('Bug Tracker', 'https://github.com/neilalbrock/sentry-bitbucket/issues'),
        ('Source', 'https://github.com/neilalbrock/sentry-bitbucket'),
    ]

    slug = 'bitbucket'
    title = _('Bitbucket')
    conf_title = title
    conf_key = 'bitbucket'
    project_conf_form = BitbucketOptionsForm
    auth_provider = 'bitbucket'

    def is_configured(self, request, project, **kwargs):
        return bool(self.get_option('repo', project))

    def get_new_issue_title(self, **kwargs):
        return 'Create Bitbucket Issue'

    def create_issue(self, request, group, form_data, **kwargs):
        auth = self.get_auth_for_user(user=request.user)

        if auth is None:
            raise forms.ValidationError(_('You have not yet associated Bitbucket with your account.'))

        repo = self.get_option('repo', group.project)

        url = u'https://api.bitbucket.org/1.0/repositories/%s/issues/' % (repo,)

        data = {
          "title": form_data['title'],
          "content": form_data['description'],
          "kind": form_data['issue_type'],
          "priority": form_data['priority']
        }

        oauth = OAuth1(unicode(settings.BITBUCKET_CONSUMER_KEY),
                        unicode(settings.BITBUCKET_CONSUMER_SECRET),
                        auth.tokens['oauth_token'], auth.tokens['oauth_token_secret'],
                        signature_type='auth_header')

        try:
            resp = requests.post(url, data=data, auth=oauth)
        except Exception, e:
            raise forms.ValidationError(_('Error communicating with Bitbucket: %s') % (e,))

        try:
            data = resp.json()
        except Exception, e:
            raise forms.ValidationError(_('Error decoding response from Bitbucket: %s') % (e,))

        return data['local_id']

    def get_issue_label(self, group, issue_id, **kwargs):
        return 'Bitbucket-%s' % issue_id

    def get_issue_url(self, group, issue_id, **kwargs):
        repo = self.get_option('repo', group.project)
        return 'https://bitbucket.org/%s/issue/%s/' % (repo, issue_id)

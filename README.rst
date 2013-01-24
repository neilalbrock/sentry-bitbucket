================
sentry-bitbucket
================

:Author: Neil Albrock
:Version: 0.1.4

An extension for Sentry which integrates with Bitbucket. Specifically, it allows you to easily create issues from events within Sentry.

This is largely a port of the ``sentry-github`` package, the main difference being that it makes use of the ``requests`` library for communication with Bitbucket and implements OAuth, which is the preferred way to integrate with their API.

IMPORTANT
=========

The ``requests-oauthlib`` project currently has some issues which have been fixed on the master branch but not yet pushed to PyPi. Until they release a new version and I can update the dependencies accordingly, you will need to run the following after installing ``sentry-bitbucket``, to ensure everything works properly::

    $ pip install -U git+git://github.com/requests/requests-oauthlib.git

Installation
============

Install the package via ``pip``::

    $ pip install sentry-bitbucket

Ensure you've configured Bitbucket auth in Sentry by adding the following to your ``sentry.conf.py``::

    # Bitbucket needs to be included as a valid auth provider
    SENTRY_AUTH_PROVIDERS = {
        'twitter': ('TWITTER_CONSUMER_KEY', 'TWITTER_CONSUMER_SECRET'),
        'facebook': ('FACEBOOK_APP_ID', 'FACEBOOK_API_SECRET'),
        'github': ('GITHUB_APP_ID', 'GITHUB_API_SECRET'),
        'google': ('GOOGLE_OAUTH2_CLIENT_ID', 'GOOGLE_OAUTH2_CLIENT_SECRET'),
        'trello': ('TRELLO_API_KEY', 'TRELLO_API_SECRET'),
        'bitbucket': ('BITBUCKET_CONSUMER_KEY', 'BITBUCKET_CONSUMER_SECRET'),
    }

    # https://bitbucket.org/account/user/<username>/api
    BITBUCKET_CONSUMER_KEY = ''
    BITBUCKET_CONSUMER_SECRET = ''

Associate your account with Bitbucket (if you haven't already) via Account -> Identities.

You'll now see a new action on groups which allows quick creation of Bitbucket issues.

Caveats
=======

If you have multiple Bitbucket identities associated in Sentry, the plugin will just select
one to use.

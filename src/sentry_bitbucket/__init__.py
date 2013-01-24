"""
sentry_bitbucket
~~~~~~~~~~~~~~~~

:copyright: (c) 2013 by Atomised Co-operative Ltd.
:license: BSD, see LICENSE for more details.
"""

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry-bitbucket').version
except Exception, e:
    VERSION = 'unknown'

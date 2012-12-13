#!/usr/bin/env python
"""
sentry-bitbucket
=============

An extension for Sentry which integrates with Bitbucket. Specifically, it
allows you to easily create issues from events within Sentry.

:copyright: (c) 2012 by Atomised Co-operative Ltd.
:license: BSD, see LICENSE for more details.
"""
from setuptools import setup, find_packages


tests_require = [
    'nose',
]

install_requires = [
    'sentry>=5.0.0',
    'requests>=0.14.0'
]

setup(
    name='sentry-bitbucket',
    version='0.1.0',
    author='Neil Albrock',
    author_email='neil@atomised.coop',
    url='https://github.com/neilalbrock/sentry-bitbucket',
    description='A Sentry extension which integrates with Bitbucket.',
    long_description=__doc__,
    license='BSD',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='runtests.runtests',
    include_package_data=True,
    entry_points={
       'sentry.apps': [
            'bitbucket = sentry_bitbucket',
        ],
       'sentry.plugins': [
            'bitbucket = sentry_bitbucket.plugin:BitbucketPlugin'
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)

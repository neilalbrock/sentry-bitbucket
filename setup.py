#!/usr/bin/env python
"""
sentry-bitbucket
================

An extension for Sentry which integrates with Bitbucket. Specifically, it
allows you to easily create issues from events within Sentry.

:copyright: (c) 2013 by Atomised Co-operative Ltd.
:license: BSD, see LICENSE for more details.
"""
import os.path
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

tests_require = [
    'nose',
]

install_requires = [
    'sentry>=5.1.0',
    'requests>=1.0.0',
    'requests-oauthlib>=0.2.0'
]

setup(
    name='sentry-bitbucket',
    version='0.1.4',
    author='Neil Albrock',
    author_email='neil@atomised.coop',
    url='https://github.com/neilalbrock/sentry-bitbucket',
    description='A Sentry extension which integrates with Bitbucket.',
    long_description=read('README.rst'),
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

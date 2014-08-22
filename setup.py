#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    'sentry>=5.3.3',
    'pygerduty>=0.22',
]

f = open('README.rst')
readme = f.read()
f.close()

setup(
    name='sentry-pagerduty',
    version='0.1.1',
    author='Depop developers',
    author_email='dev@depop.com',
    url='https://github.com/depop/sentry-pagerduty',
    description='A Sentry plugin for sending error occurrences to a PagerDuty instance.',
    long_description=readme,
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'sentry.plugins': [
            'sentry_pagerduty = sentry_pagerduty.plugin:PagerDutyPlugin'
        ],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development',
        'FOR INTERNAL RELEASE ONLY', # To prevent accidental upload to pypi
    ],
    keywords='sentry pagerduty',
)

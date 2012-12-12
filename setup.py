# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='amount-in-words',
    version='0.1.0',
    description='Convert amount to words (Polish translation).',
    author='Adam Bogdal',
    author_email='adam@bogdal.pl',
    url = 'https://github.com/bogdal/amount-in-words',
    download_url='https://github.com/bogdal/amount-in-words/zipball/master',
    packages=find_packages(),
    include_package_data=True,
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Topic :: Utilities'
    ],
    zip_safe = False,
    test_suite = "amount_in_words.tests"
)
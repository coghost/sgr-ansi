#!/usr/bin/env python

from setuptools import setup, find_packages
from sgr_ansi import VERSION

setup(
    name='sgr-ansi',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.tpl', '*.md']},
    author='lihe',
    author_email='imanux@sina.com',
    url='https://github.com/coghost/sgr-ansi',
    description='awesome ansi8 colorful text interface in terminal',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    license='GPL',
    install_requires=[],
    project_urls={
        'Bug Reports': 'https://github.com/coghost/sgr-ansi/issues',
        'Source': 'https://github.com/coghost/sgr-ansi',
    },
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords=['sgr', 'ansi', 'colorful', 'vivid', 'awesome', 'terminal'],
)

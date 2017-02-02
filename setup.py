#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io

from setuptools import setup, find_packages


long_description = '\n'.join((
    io.open('README.rst').read(),
    io.open('CHANGELOG.rst').read(),
    ''
))

setup(
    name='pelican-social',
    version=__import__('social').__version__,
    description=__import__('social').__description__,
    long_description=long_description,
    url='https://github.com/noirbizarre/pelican-social',
    author='Axel Haustant',
    author_email='noirbizarre+pelican@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['pelican>=3.7.0'],
    license='LGPL',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: System :: Software Distribution",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Software Development :: Libraries :: Python Modules",
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    ],
)

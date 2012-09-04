#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time-stamp: <11-Jul-2012 10:30:59 PDT by rich.pixley@palm.com>

# Copyright (c) 2010 - 2012 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='rcmp',
    version='0.006',
    author='Rich Pixley',
    author_email='rich.pixley@palm.com',
    description='A more flexible, filecmp replacement.',
    license='PROPRIETARY',
    keywords='',
    url='',
    long_description=read('README'),
    setup_requires=[
    	'nose>=0.11.1',
    ],
    install_requires=[
    ],
    packages=find_packages(),
    include_package_data=True,
    test_suite='nose.collector',
    py_modules=['rcmp'],
    requires=[
        'collections',
        'os',
    ],
    provides=[
        'rcmp',
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

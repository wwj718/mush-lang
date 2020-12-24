#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""

from setuptools import setup, find_packages

readme = """
mush-lang
"""

history = ""

REQUIRES_PYTHON = ">=3.6.0"
requirements = ['pyzmq', 'msgpack-python', 'loguru', 'uflash', "zeroconf", "click"]

setup_requirements = [
    'pytest-runner',
]

test_requirements = ['pytest', 'pytest-mock']

setup(
    python_requires=REQUIRES_PYTHON,
    author="Wenjie Wu",
    author_email='wuwenjie718@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',

    ],
    description="",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mush_lang',
    name='mush_lang',
    packages=[
        'mush_lang', 'mush_lang.tools'
    ],  # find_packages(include=['codelab_adapter_client','codelab_adapter_client.tools']),
    entry_points={
        'console_scripts': [
            'mush-lang = mush_lang.tools.cli:main',
        ],
    },
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/wwj718/mush_lang',
    version='0.0.1',
    zip_safe=False,
)

#!/usr/bin/env python
"""
{{cookiecutter.project_name}}
=====

"""

import {{cookiecutter.project_name}}
from setuptools import setup, find_packages
import sys

install_requires = [
    "Django==1.8.2",
    "raven==5.2.0",
]

dev_requires = [
    'django-debug-toolbar',
]

test_requires = [
    "pytest",
    "pytest-cov",
    "pytest-django",
]


setup(
    name="{{cookiecutter.project_name}}",
    version={{cookiecutter.project_name}}.__version__,
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    url="",
    description="{{cookiecutter.description}}",

    # Packages and data to take into account
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,

    zip_safe=False,  # Avoid eggs

    # Allow pip install .[tests,dev] to install the dev and test dependencies
    extras_require={
        "tests": test_requires,
        "dev": dev_requires,
    },
    install_requires=install_requires,
    tests_require=test_requires,
)

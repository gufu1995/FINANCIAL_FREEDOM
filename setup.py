#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = "financial_freedom",
    version = "0.0.1",
    packages = find_packages( where = "src" ),
    package_dir = {
        "": "src"
    },
    install_requires = [
        "matplotlib>=3.10.0",
        "matplotlib-inline>=0.1.7",
        "numpy>=2.2.3",
        "pandas>=2.2.3",
    ],
    extra_requires = {
        "test": [ "pytest>=6.2.5",]
    },
    entry_points = {
        "console_scripts": [ "financial_freedom=financial_freedom.main:main",],
    },
    author = "Gunnar Fuchs",
    author_email = "Gunnar.Fuchs1995@gmail.com",
    description = "A project for achieving financial freedom.",
    long_description = open( "README.md" ).read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/gufu1995/FINANCIAL_FREEDOM",
    license = "MIT",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)

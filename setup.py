#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="RangeMinQuery",
    packages=["RangeMinQuery"],
    version="0.1.2",
    description="Solving the Range Minimum Query problem",
    author="Chuancong Gao",
    author_email="chuancong@gmail.com",
    url="https://github.com/chuanconggao/RangeMinQuery",
    download_url="https://github.com/chuanconggao/RangeMinQuery/tarball/0.1.2",
    keywords=[
        "range minimum query"
    ],
    license="MIT",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
    install_requires=[
        "future>=0.16.0",
    ]
)

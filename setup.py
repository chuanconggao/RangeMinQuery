#! /usr/bin/env python3

from setuptools import setup

url = "https://github.com/chuanconggao/RangeMinQuery"
version = "0.2"

setup(
    name="RangeMinQuery",

    packages=["RangeMinQuery"],
    include_package_data=True,

    url=url,

    version=version,
    download_url=f"{url}/tarball/{version}",

    license="MIT",

    author="Chuancong Gao",
    author_email="chuancong@gmail.com",

    description="Solving the Range Minimum Query problem",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",

    keywords=[
        "range-minimum-query",
    ],
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],

    install_requires=[
        line.strip() for line in open("requirements.txt")
    ]
)

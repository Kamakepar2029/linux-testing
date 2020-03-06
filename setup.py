#!/usr/bin/env python2
from setuptools import setup

setup(
    name = "kamakepar-gen",
    version = "0.1",
    author = "Kama Kepar",
    description = "Generate A FILE",
    keywords = "geenerate, file",
    url = "https://github.com/Kamakepar2029/linux-testing",
    scripts=['gen'],
    # py_modules=['wifijammer'],
    install_requires=['scapy'],
    long_description="Generate a long big distructive file",
    classifiers=[
        "Development Status :: 1 - Beta",
        "Topic :: Utilities",
    ],
)

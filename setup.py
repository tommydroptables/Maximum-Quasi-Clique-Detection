# Licensed Materials - Property of IBM
# (C) Copyright IBM Corp. 2011, 2013. All Rights Reserved.
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

__author__ = 'Tom Cocozzello'

from setuptools import setup

setup(
    # Application name:
    name="quasiclique",

    # Version number (initial):
    version="1.0",

    # Application author details:
    author="Thomas Cocozzello",
    author_email="thomas.cocozzello@gmail.com",

    # Packages
    packages=[
    ],

    # Include additional files into the package
    include_package_data=True,
    description="Maximum Quasi Clique Detection",

    # Dependent packages (distributions)
    # To install igraph i needed to run
    #   sudo apt-get install libxml2-dev --upgrade
    #   sudo apt-get install libxml2
    install_requires=[
        "python-igraph",
        "numpy",
        "cairocffi"
    ],
)

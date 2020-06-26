# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 14:17:22 2020

@author: DANIEL
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csv_json", # Replace with your own username
    version="0.0.2",
    author="Daniel, Harish",
    author_email="teamcoders21@gmail.com",
    description="A package to convert csv files to json and vice-versa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TeamCoders02/csv_json",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

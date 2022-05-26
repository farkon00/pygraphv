#!/usr/bin/env python

import setuptools

with open("D:\pygraphv\PYPIREADME.md", "r") as fh:
    long_description = fh.read()

if __name__ == '__main__':
    setuptools.setup(
        name="pygraphv", 
        version="0.2", 
        author="farkon00",
        author_email="sammer2016sammer@gmail.com",
        description="Python library for generating dot programming language for creating graphviz graphs from python OO style code.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/farkon00/pygraphv",
        packages=setuptools.find_packages(),
        python_requires=">=3.6",
        license="MIT",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
    )

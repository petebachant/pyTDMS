#!/usr/bin/env python
# coding=utf-8

from distutils.core import setup

setup(
    name='pyTDMS',
    version='0.0.2',
    author='Floris van Vugt',
    author_email='F.T.vanVugt@gmail.com',
    py_modules=['pytdms'],
    scripts=[],
    url='https://github.com/petebachant/pyTDMS.git',
    license='GPL v2',
    description='Module for reading National Instruments TDMS files.',
    long_description=open('README.md').read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4"]
)

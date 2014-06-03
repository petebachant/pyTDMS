#!/usr/bin/env python
# coding=utf-8

from distutils.core import setup

setup(
    name='pyTDMS',
    version='0.0.2',
    author='Floris van Vugt',
    modules=['pytdms'],
    scripts=[],
    url='https://github.com/petebachant/pyTDMS.git',
    license='LICENSE',
    description='Module for reading National Instruments TDMS files.',
    long_description=open('README.md').read(),
)

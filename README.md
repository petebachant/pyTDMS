pyTDMS
======

A fork of the pyTDMS module for reading National Instruments TDMS files with Python,
originally written by Floris van Vugt.

Installation
------------

Execute `python setup.py install` inside this directory.

Usage
-----

```python
import pytdms

objects, rawdata = pytdms.read(filename)
```
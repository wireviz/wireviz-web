#!/usr/bin/env python

# This is a shim to allow GitHub to detect the package
# and build the "Dependents" list.
# https://github.com/wireviz/wireviz-web/network/dependents

import setuptools

if __name__ == "__main__":
    setuptools.setup(name="wireviz-web")

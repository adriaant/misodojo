#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="misodojo",
    version="1.0",
    description="Simple blogging",
    author="Adriaan Tijsseling",
    author_email="adriaangt@gmail.com",
    url="",
    packages=find_packages(),
    package_data={"misodojo": ["static/*.*", "templates/*.*"]},
    scripts=["manage.py"],
)

#!/usr/bin/env python
# encoding: utf-8
# @Author: Draco
# @Time  : 2017/10/9 14:25

from setuptools import setup,find_packages

setup(
    name='flaskr',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
],
)
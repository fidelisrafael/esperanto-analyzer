# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='esperanto-analyzer',
    version='0.0.1',
    description='My tries on creating one Esperanto lingvo analyzer',
    long_description=readme,
    author='Rafael Fidelis',
    author_email='rafa_fidelis@yahoo.com.br',
    url='https://github.com/fidelisrafael',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


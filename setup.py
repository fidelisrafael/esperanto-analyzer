# pylint: disable=missing-docstring,no-self-use,invalid-name

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    lib_license = f.read()

with open('requirements.txt') as fd:
    requirements = [line.rstrip() for line in fd]

with open('development_requirements.txt') as fd:
    requirements.append([line.rstrip() for line in fd])

with open('test_requirements.txt') as fd:
    test_requirements = [line.rstrip() for line in fd]

setup(
    name='esperanto-analyzer',
    version='0.0.1',
    description='My tries on creating one Esperanto lingvo analyzer',
    long_description=readme,
    author='Rafael Fidelis',
    author_email='rafa_fidelis@yahoo.com.br',
    url='https://github.com/fidelisrafael/esperanto-analyzer',
    license=lib_license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requirements,
    tests_require=test_requirements,
)

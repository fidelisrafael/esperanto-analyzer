# pylint: disable=missing-docstring,no-self-use,invalid-name

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    lib_license = f.read()

with open('requirements.txt') as fd:
    requirements = [line.rstrip() for line in fd]

with open('test_requirements.txt') as fd:
    test_requirements = [line.rstrip() for line in fd]

setup(
    name='esperanto-analyzer',
    version='0.0.3',
    description='Morphological and syntactic analysis of Esperanto sentences.',
    long_description=readme,
    author='Rafael Fidelis',
    author_email='rafaelfid3lis@gmail.com',
    url='https://github.com/fidelisrafael/esperanto-analyzer',
    license=lib_license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requirements,
    tests_require=test_requirements,
    classifiers=[
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3",
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

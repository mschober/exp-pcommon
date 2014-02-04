from setuptools import setup, find_packages
import sys, os, multiprocessing

version = '0.1'

setup(
    name='common',
    version=version,
    description="common package",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    setup_requires=['setuptools_git'],
    test_requires=['nose'],
    test_suite="nose.collector",
    tests_require="nose",
)

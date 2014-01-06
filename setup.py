from setuptools import setup, find_packages
import sys, os, multiprocessing

version = '0.1'

setup(
    name='common',
    version=version,
    description="common package",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    setup_requires=['nose>=1.0'],
    test_suite="nose.collector",
    tests_require="nose",
)

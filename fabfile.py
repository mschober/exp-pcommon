#!/usr/bin/env python

from fabric.api import *


def setup_tox():
    local('tox-quickstart')

def test():
    local('tox')

def freeze():
    local('pip freeze | tee requirements.txt')

def develop():
    local('python setup.py develop')

def build():
    local('python setup.py build')

def install():
    local('pip install -r requirements.txt --upgrade')

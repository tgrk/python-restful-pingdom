from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "pingdom",
    version = "1.0",
    packages = find_packages(),
    author = "Dan Craig",
    author_email = "drcraig@gmail.com",
    description = "Python Module for Pingdom REST API",
    license = "MIT",
    keywords = "pingdom alerts",
    url = "https://github.com/drcraig/python-restful-pingdom/"
)

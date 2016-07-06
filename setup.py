"""
use 'conda setup.py develop' while in file folder in anaconda to install this package
"""

from setuptools import setup, find_packages

setup(
    name='2016_summer_XPD',
    version='0.0.2',
    install_requires=['tifffile', 'matplotlib', 'numpy'],
    packages=find_packages(),
    description='Experimental code for summer project',
    zip_safe=False,
    url='https://github.com/cduff4464/2016_summer_XPD.git'
)

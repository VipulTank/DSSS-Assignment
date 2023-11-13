from distutils.core import setup
from setuptools import find_packages

setup( name="DSSS Homework2",
      version="0.1", 
      author="Vipul", 
      author_email="tankvipul18@gmail.com",
      packages=find_packages(),
      install_requires=["numpy", "turtles"] )

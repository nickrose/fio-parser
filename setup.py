# -*- coding: utf-8 -*-
"""Setup package."""
# See https://packaging.python.org/distributing/
# and https://github.com/pypa/sampleproject/blob/master/setup.py

try:
    from setuptools import setup, find_packages
    pkgs = find_packages()
except ImportError:
    from distutils.core import setup
    pkgs = ['libfioparser']

try:
    from pip.req import parse_requirements
    install_reqs = parse_requirements('./requirements.txt')
    reqs = [str(ir.req) for ir in install_reqs]
except ImportError:
    reqs = ['numpy', 'hurry']

with open('README.md') as f:
        readme = f.read()

setup(name='fioparser',
      # version=__version__,
      description=('FIO test result parsing'),
      # author=__author__,
      # author_email=__email__,
      url='https://github.com/nickrose/fio-parser',
      license='GPLv2',
      packages=pkgs,
      install_requires=reqs,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6'
      ],
      )

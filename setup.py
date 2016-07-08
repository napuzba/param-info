# Copyright (C) 2016 Napuzba [kobi@napuzba.com]
# Licensed under MIT license [http://openreq.source.org/licenses/MIT]

from setuptools import setup

description = 'param_info is python package for parsing parameters'
long_description = '''
=====
About
=====

********
Features
********

*****
Usage
*****
'''

setup(
  name             = 'param-info',
  packages         = ['param_info'],
  install_requires = [
     'urllib3 >= 1.0',
  ],
  version          = '2.1.1',
  author           = 'napuzba',
  author_email     = 'kobi@napuzba.com',
  url              = 'https://github.com/napuzba/param-info.git',
  download_url     = 'https://github.com/napuzba/param-info/releases',
  description      = description,
  long_description = long_description,
  license          = 'MIT',
  keywords         = ['download,crawl,ftp,http'],
  classifiers      = [
    'Topic :: Software Development :: Libraries :: Python Modules',

    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',

    'Development Status :: 3 - Alpha'
  ],
)

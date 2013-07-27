#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Hua Liang[Stupid ET] <et@everet.org>
#

from distutils.core import setup, Extension

libs = ['user32']

setup(name='etHook',
      version='0.0.1',
      author='Hua Liang',
      author_email='et@everet.org',
      url='http://',
      download_url='http://',
      license='http://www.opensource.org/licenses/mit-license.php',
      platforms=['Win32'],
      description='',
      long_description='',
      packages=['etHook'],
      package_dir={'etHook': ""},
      ext_modules=[Extension('etHook._example', ['example.c', 'example.i'], libraries=libs)],
      # data_files=[('Lib/site-packages/etHook', ['LICENSE.txt', 'README.txt', 'CHANGELOG.txt'])]
      )

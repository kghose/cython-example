from setuptools import setup
from Cython.Build import cythonize

setup(
    name='kgcyex',
    version='1.0.0',
    packages=['kgcyex', 'kgcyex.lib'],
    entry_points={
      # Command line scripts
      'console_scripts': ['kgcyex = kgcyex.main:cli']
    },
    install_requires=[
      'setuptools>=0.7',
    ],
    ext_modules=cythonize(['cy1.pyx', 'lib/cy2.pyx']),
    test_suite='nose.collector'
)
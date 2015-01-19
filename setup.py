from setuptools import setup
from Cython.Build import cythonize

setup(
    name='kgcyex',
    version='1.0.1',
    packages=['kgcyex', 'kgcyex.lib'],
    entry_points={
      # Command line scripts
      'console_scripts': ['kgcyex = kgcyex.main:cli']
    },
    install_requires=[
      'setuptools>=0.7',
    ],
    ext_modules=cythonize(['kgcyex/cy1.pyx', 'kgcyex/lib/cy2.pyx'])
)
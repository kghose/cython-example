from setuptools import setup, Extension

try:
  from Cython.Build import cythonize
  USE_CYTHON = True
except ImportError:
  USE_CYTHON = False

ext = '.pyx' if USE_CYTHON else '.c'
extensions = [Extension("kgcyex.cy1", ["kgcyex/cy1"+ext]), Extension("kgcyex.lib.cy2", ["kgcyex/lib/cy2"+ext])]
if USE_CYTHON:
    extensions = cythonize(extensions)

setup(
    name='kgcyex',
    version='1.0.3',
    packages=['kgcyex', 'kgcyex.lib'],
    entry_points={
      # Command line scripts
      'console_scripts': ['kgcyex = kgcyex.main:cli']
    },
    install_requires=[
      'setuptools>=0.7',
    ],
    ext_modules=extensions
)
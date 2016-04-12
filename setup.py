
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# typing library was introduced as a core module in version 3.5.0
requires = ['rdflib']
if sys.version_info < (3, 5):
    requires.append("typing")

setup(
    name='dbgap_to_owl',
    version='0.1.1',
    packages=['dbgap_to_owl'],
    url='http://github.com/crDDI/dbgap_to_owl',
    license='Apache License 2.0',
    author='Harold Solbrig',
    author_email='solbrig.harold@mayo.edu',
    description='Utility to convert dbgap schema to OWL representation',
    long_description='Convert dbGaP schema to OWL',
    install_requires=requires,
    scripts=['scripts/dbgaptoowl'],
    classifiers=[
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only']
)

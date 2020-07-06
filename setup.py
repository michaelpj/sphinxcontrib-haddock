import sys, os

from setuptools import setup, find_packages

requires = ['sphobjinv>=2.0', 'sphinxcontrib-domaintools>=0.3']

setup(
    name='sphinxcontrib-haddock',
    version='0.1',
    url='',
    download_url='',
    license='MIT',
    author='Michael Peyton Jones',
    author_email='me@michaelpj.com',
    description='',
    long_description='',
    zip_safe=False,
    classifiers=[],
    platforms='any',
    packages=find_packages(),
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
    entry_points={"console_scripts": ["haddock_inventory = sphinxcontrib.haddock_inventory:main"]},
)

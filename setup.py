#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name='dog',
    version='1.0.0',
    description='dog > cat',
    url='https://github.com/alistairking/dog',
    packages=setuptools.find_packages(),
    install_requires=[
        'smart-open[all]',
    ],
    entry_points={'console_scripts': [
        'dog = dog.dog:main',
    ]}
)

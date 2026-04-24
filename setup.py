# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="python-signify",
    version='0.2.0',
    url='https://github.com/bjornedstrom/python-signify',
    license='MIT',
    description="OpenBSD Signify for Python",
    author=u'Björn Edström',
    author_email='be@bjrn.se',
    packages=['signify'],
    classifiers=[
        'Operating System :: Unix',
        'Topic :: Security :: Cryptography',
    ],
    install_requires=[
        'py-bcrypt',
        'nacl'
    ],
    scripts=[
        'bin/signi.py',
        'bin/signipie',
    ]
)

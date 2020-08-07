#! /usr/bin/env python

"""
Setup file for tstat_transport distribution.
"""

import sys
from setuptools import setup
import os


try:
    # Use pandoc to convert .md -> .rst when uploading to pypi
    import pypandoc
    DESCRIPTION = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError, OSError):
    DESCRIPTION = open('README.md').read()

if sys.version_info[0] == 2 and sys.version_info[1] < 6:
    sys.exit('Sorry, Python < 2.6 is not supported')

if sys.version_info[0] == 3 and sys.version_info[1] < 3:
    sys.exit('Sorry, Python 3 < 3.3 is not supported')


# use requirements.txt to define dependencies
def get_required():
    with open('requirements.txt') as f:
        required = f.read().splitlines()
    return required


setup(
    name='tstat_transport',
    version='0.6.8',
    description='Tools to send Tstat (TCP STatistic and Analysis Tool) log data to archive servers.',  # pylint: disable=line-too-long
    long_description=DESCRIPTION,
    author='Monte M. Goode',
    author_email='MMGoode@lbl.gov',
    url='https://github.com/esnet/tstat-transport',
    packages=['tstat_transport'],
    scripts=[
        'bin/tstat_send',
        'bin/tstat_cull',
    ],
    install_requires=get_required(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet',
        'Topic :: System :: Networking',
        'Topic :: Software Development :: Libraries',
    ],
)

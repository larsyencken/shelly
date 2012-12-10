# -*- coding: utf-8 -*-
#
#  setup.py
#  shelly
#

"""
Package information for shelly package.
"""

from setuptools import setup

VERSION = '0.2.1'

setup(
        name='shelly',
        description="Standalone tools to make the shell better.",
        long_description="""
Shelly makes processing line-by-line data in the shell easier, by providing
access to useful functional programming primitives and interactive tools.
""",
        url="http://bitbucket.org/larsyencken/shelly/",
        version=VERSION,
        author="Lars Yencken",
        author_email="lars@yencken.org",
        license="BSD",
        scripts=[
            'shelly',
        ],
        packages=[
            'shelly_cmd',
        ],
        install_requires=[
            'clint',  # 0.3.1
            'consoleLog==0.2.4',
        ],
    )

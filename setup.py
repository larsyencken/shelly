# -*- coding: utf-8 -*-
#
#  setup.py
#  shelly
#
#  Created by Lars Yencken on 2012-03-05.
#  Copyright 2012 Lars Yencken. All rights reserved.
#

"""
Package information for shelly package.
"""

from setuptools import setup

VERSION = '0.1.0'

setup(
        name='shelly',
        description="Standalone tools to make the shell better.",
        long_description=\
"""
Shelly makes processing line-by-line data in the shell easier, by providing
access to useful functional programming primitives and interactive tools.
""",
        url="http://bitbucket.org/larsyencken/shelly/",
        version=VERSION,
        author="Lars Yencken",
        author_email="lars@yencken.org",
        license="BSD",
        scripts=[
            'drop',
            'take',
            'groupby',
            'random',
            'max',
            'trickle',
        ],
    )

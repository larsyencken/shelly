#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  normspace.py
#  shelly
#

"""
Normalise spaces from the lines on stdin, stripping outer spaces and
converting all sequences of spaces or tabs into single spaces.
"""

import sys
import optparse
import re


def normspace(istream=sys.stdin, ostream=sys.stdout):
    for l in istream:
        l = l.strip()
        l = re.sub('[ \t]+', ' ', l)
        print >> ostream, l


def _create_option_parser():
    usage = \
"""%prog normspace [options]

Normalises whitespace in lines from stdin. Strips outer spaces and replaces
any sequences of whitespace with a single space."""

    parser = optparse.OptionParser(usage)

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if args:
        parser.print_help()
        sys.exit(1)

    try:
        normspace(*args)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main(sys.argv[1:])

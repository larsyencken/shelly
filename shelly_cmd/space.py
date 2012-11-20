#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  space.py
#  shelly
#

"""
Insert spaces between lines.
"""

import sys
import optparse


def space(istream=sys.stdin, ostream=sys.stdout):
    for i, l in enumerate(istream):
        if i > 1:
            ostream.write('\n')
        ostream.write(l)


def _create_option_parser():
    usage = \
"""%prog space [options]

Adds a newline between all pairs of lines from stdin. This is especially
useful if debugging the output of very long lines, wrapped in the terminal."""

    parser = optparse.OptionParser(usage)

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if args:
        parser.print_help()
        sys.exit(1)

    space(*args)


if __name__ == '__main__':
    main(sys.argv[1:])

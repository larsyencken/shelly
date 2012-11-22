#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  join.py
#  shelly
#

"""
A simple string join.
"""

import sys
import optparse


def join(delimiter, istream=sys.stdin, ostream=sys.stdout):
    print >> ostream, delimiter.join(l.strip() for l in istream)


def _create_option_parser():
    usage = \
"""%prog join [options] <delimiter>

Join all lines on stdin with the delimiter into a single line on stdout."""

    parser = optparse.OptionParser(usage)

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if len(args) != 1:
        parser.print_help()
        sys.exit(1)

    join(*args)


if __name__ == '__main__':
    main(sys.argv[1:])

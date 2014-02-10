#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  normjson.py
#  shelly
#

"""
Convert one-record-per-line JSON into a single JSON record.
"""

import sys
import optparse


def normjson(istream=sys.stdin, ostream=sys.stdout):
    ostream.write('[')
    comma = False
    for l in istream:
        if comma:
            ostream.write(', ')
        ostream.write(l)
        comma = True
    print >> ostream, ']'


def _create_option_parser():
    usage = \
"""%prog join [options]

Convert one-record-per-line JSON into a single JSON record."""

    parser = optparse.OptionParser(usage)

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if args:
        parser.print_help()
        sys.exit(1)

    normjson(*args)


if __name__ == '__main__':
    main(sys.argv[1:])

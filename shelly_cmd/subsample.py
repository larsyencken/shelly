#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  subsample.py
#  shelly
#

"""
Take only a subset of lines from stdin.
"""

import sys
import optparse
import random


def subsample(p, istream=sys.stdin, ostream=sys.stdout):
    r = random.random
    write = ostream.write
    for l in istream:
        if r() < p:
            write(l)


def _create_option_parser():
    usage = \
"""%prog subsample [options] p

Prints to stdout a subsample of lines from stdin, of proportion given by p.
For example, using 0.4 will keep roughly 40% of input lines."""

    parser = optparse.OptionParser(usage)

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if len(args) != 1:
        parser.print_help()
        sys.exit(1)

    p = float(args[0])
    if not (0 < p < 1):
        print >> sys.stderr, 'must provide 0 < p < 1'
        parser.print_help()
        sys.exit(1)
    subsample(p)


if __name__ == '__main__':
    main(sys.argv[1:])

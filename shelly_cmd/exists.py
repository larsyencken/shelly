#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exists.py
#  shelly
#

import os
import sys
import optparse


def exists(invert=False):
    ope = os.path.exists
    for l in sys.stdin:
        filename = l.strip()
        if ope(filename) ^ invert:
            print filename


def _create_option_parser():
    usage = \
"""%prog exists [options]

Filter out files from stdin which don't exist."""

    parser = optparse.OptionParser(usage)
    parser.add_option('--invert', action='store_true', dest='invert',
            help="Only list files which don't exist", default=False)

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if args:
        parser.print_help()
        sys.exit(1)

    exists(invert=options.invert)


if __name__ == '__main__':
    main(sys.argv[1:])

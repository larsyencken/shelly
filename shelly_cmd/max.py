#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  max.py
#  shelly
#

"""
Calculate a running maximum and display to stdout.
"""

import sys
import optparse

from consoleLog.slot import Slot


def running_max(istream=sys.stdin):
    print '%18s' % 'max'
    s = Slot()
    m = float('-inf')
    try:
        for line in sys.stdin:
            v = float(line)
            if v > m:
                m = v
                s.update('%18s' % str(m))
    except KeyboardInterrupt:
        pass
    except IOError:
        pass
    s.update(str(m))

    print


def _create_option_parser():
    usage = \
"""%prog max [options]

Displays a running maximum of values from stdin."""

    parser = optparse.OptionParser(usage)

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if args:
        parser.print_help()
        sys.exit(1)

    running_max(*args)


if __name__ == '__main__':
    main(sys.argv[1:])

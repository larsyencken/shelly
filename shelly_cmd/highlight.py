#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  highlight.py
#  shelly
#

"""
Highlight the matching regular expression in each line.
"""

import sys
import optparse
import re

from clint.textui import colored
from clint.packages import colorama


def highlight(pattern, istream=sys.stdin, ostream=sys.stdout, color='red'):
    if color not in colored.COLORS:
        raise ValueError('expected one of red/blue/green, got %s' % color)
    color = color.upper()
    regex = re.compile(pattern)
    for l in istream:
        matches = [m.span() for m in regex.finditer(l)]
        if not matches:
            ostream.write(l)
        else:
            matches.reverse()
            i = 0
            while matches:
                start, stop = matches.pop()
                ostream.write(l[i:start])
                ostream.write('%s%s%s' % (
                        getattr(colorama.Fore, color),
                        l[start:stop],
                        colorama.Fore.RESET,
                    ))
                i = stop
            ostream.write(l[i:])


def _create_option_parser():
    usage = \
"""%prog highlight [options] pattern

Operates like a mixture of grep and cat. Passes stdin through to stdout, but
highlighting the given pattern wherever it's found."""

    parser = optparse.OptionParser(usage)
    parser.add_option('--blue', action='store_true', dest='blue')
    parser.add_option('--red', action='store_true', dest='red',
            default=True)
    parser.add_option('--green', action='store_true', dest='green')

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if len(args) != 1:
        parser.print_help()
        sys.exit(1)

    color = 'blue' if options.blue else 'green' if options.green else 'red'
    highlight(*args, color=color)


if __name__ == '__main__':
    main(sys.argv[1:])

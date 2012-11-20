#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  take.py
#  shelly
#

"""
Take lines from the input until they match a given regex.
"""

import sys
import optparse
import re


def take(regex, until=True):
    search = re.compile(regex).search
    write = sys.stdout.write
    if until:
        for line in sys.stdin:
            if search(line):
                break
            write(line)
    else:
        for line in sys.stdin:
            if not search(line):
                break
            write(line)


def _create_option_parser():
    usage = \
"""%prog take [options]

Cat a prefix of lines from stdin until some cutoff criteria is met."""

    parser = optparse.OptionParser(usage)
    parser.add_option('--until', action='store', dest='until_regex',
            help='Stop at the first line which matches this regex.')
    parser.add_option('--while', action='store', dest='while_regex',
            help='Stop at the first line which doesn\'t match this regex.')

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if args or not (bool(options.until_regex) ^ bool(options.while_regex)):
        parser.print_help()
        sys.exit(1)

    regex = options.until_regex or options.while_regex

    take(regex, until=bool(options.until_regex))


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass
    except IOError:
        pass

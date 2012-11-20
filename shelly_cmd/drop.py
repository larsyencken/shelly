#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  drop.py
#  shelly
#

"""
Drop a prefix of lines from stdin which match a pattern.
"""

import sys
import optparse
import re


def drop(regex, istream=sys.stdin, ostream=sys.stdout, until=False):
    search = re.compile(regex).search
    write = ostream.write
    if until:
        for line in istream:
            if search(line):
                write(line)
                break
    else:
        for line in istream:
            if not search(line):
                write(line)
                break

    for line in istream:
        write(line)


def _create_option_parser():
    usage = \
"""%prog drop [options]

Drop a prefix of lines from stdin until some cutoff criteria is met."""

    parser = optparse.OptionParser(usage)
    parser.add_option('--until', action='store', dest='until_regex',
            help='Drop until the first line which matches this regex.')
    parser.add_option('--while', action='store', dest='while_regex',
            help='Drop until we find a line which doesn\'t match.')

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if args or not (bool(options.until_regex) ^ bool(options.while_regex)):
        parser.print_help()
        sys.exit(1)

    regex = options.until_regex or options.while_regex
    drop(regex, until=bool(options.until_regex))


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass
    except IOError:
        pass

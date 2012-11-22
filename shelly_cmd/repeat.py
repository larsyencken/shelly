#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  repeat.py
#  shelly
#

"""
Repeat a command a given number of times (or, infinitely).
"""

import sys
import optparse
import subprocess


def repeat(cmd_args, n=None):
    run = lambda: subprocess.Popen([' '.join(cmd_args)], stdout=sys.stdout,
            stderr=sys.stderr, shell=True)
    if n is None:
        while True:
            run()

    else:
        while n > 0:
            run()
            n -= 1


def _create_option_parser():
    usage = \
"""%prog repeat [options] <command string>

Runs the given shell command over and over indefinitely, or N times with the
-n option. If the command has arguments, include it and them in a single quoted
string."""

    parser = optparse.OptionParser(usage)
    parser.add_option('-n', action='store', dest='n', default=None,
            type='int', help='Finish after n iterations.')

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if not args:
        parser.print_help()
        sys.exit(1)

    try:
        repeat(args, n=options.n)
    except (KeyboardInterrupt, IOError):
        pass


if __name__ == '__main__':
    main(sys.argv[1:])

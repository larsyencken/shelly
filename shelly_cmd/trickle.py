#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trickle.py
#  shelly
#

"""
Trickle data in, line by line, at the given rate.
"""

import sys
import optparse
import random
import time
import math


def trickle(rate, istream=sys.stdin, ostream=sys.stdout):
    write = ostream.write
    try:
        for line in istream:
            wait_exponentially(rate)
            write(line)
    except KeyboardInterrupt:
        # why make a fuss?
        pass


def trickle_unbuffered(rate, istream=sys.stdin, ostream=sys.stdout):
    "Read using unbuffered methods and flush after every line."
    write = ostream.write
    flush = ostream.flush
    try:
        l = istream.readline()
        while l:
            wait_exponentially(rate)
            write(l)
            flush()
            l = istream.readline()
    except KeyboardInterrupt:
        # why make a fuss?
        pass


def wait_exponentially(rate):
    cdf = random.random()
    wait = rate * -math.log(1 - cdf)
    time.sleep(wait)


def _create_option_parser():
    usage = \
"""%prog trickle [options] <rate>

Delay incoming data according to the given rate."""

    parser = optparse.OptionParser(usage)
    parser.add_option('-u', action='store_true', dest='unbuffered',
            help='Run with reduced buffering.')

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if len(args) != 1:
        parser.print_help()
        sys.exit(1)

    rate = float(args[0])
    if options.unbuffered:
        trickle_unbuffered(rate)
    else:
        trickle(rate)


if __name__ == '__main__':
    main(sys.argv[1:])

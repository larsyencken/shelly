#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  range.py
#  shelly
#

"""
Calculate a running range and display to stdout.
"""

import sys
import optparse
import datetime


from consoleLog.slot import Slot


def running_timestamps(istream=sys.stdin, strict=False):
    print '%21s %21s %12s' % ('min', 'max', 'delta')
    s = Slot()
    _min = sys.maxint
    _max = 0
    fromtimestamp = datetime.datetime.utcfromtimestamp
    try:
        for line in sys.stdin:
            try:
                v = int(line)
            except ValueError, e:
                if not strict:
                    continue
                raise e
            dirty = False
            if v < _min:
                _min = v
                dirty = True
            if v > _max:
                _max = v
                dirty = True

            if dirty:
                s.update('%21s %21s %12s' % (
                    fromtimestamp(_min),
                    fromtimestamp(_max),
                    humanise(_max - _min),
                ))
    except KeyboardInterrupt:
        pass
    except IOError:
        pass
    s.update('%21s %21s %12s' % (
        fromtimestamp(_min),
        fromtimestamp(_max),
        humanise(_max - _min),
    ))

    print


def running_range(istream=sys.stdin, strict=False):
    print '%18s %18s %18s' % ('min', 'max', 'delta')
    s = Slot()
    _min = float('inf')
    _max = float('-inf')
    try:
        for line in sys.stdin:
            try:
                v = float(line)
            except ValueError, e:
                if not strict:
                    continue
                raise e
            dirty = False
            if v < _min:
                _min = v
                dirty = True
            if v > _max:
                _max = v
                dirty = True

            if dirty:
                s.update('%18s %18s %18s' % (_min, _max, _max - _min))
    except KeyboardInterrupt:
        pass
    except IOError:
        pass
    s.update('%18s %18s %18s' % (_min, _max, _max - _min))

    print


def humanise(s):
    d = datetime.timedelta(seconds=s)
    if d.days > 3:
        return '%d days' % (d.days)

    if d.days > 0:
        return '%d hours' % (s / 3600)

    if s / 3600 > 1:
        return '%d hours %d min' % divmod(s / 60, 60)

    return '%d min' % (s / 60)


def _create_option_parser():
    usage = \
"""%prog range [options]

Displays a running maximum of values from stdin."""

    parser = optparse.OptionParser(usage)
    parser.add_option('--strict', action='store_true', dest='strict',
            help='Fail on non-numeric input, rather than skipping it.')
    parser.add_option('-t', '--timestamps', action='store_true',
            dest='timestamps',
            help='Treat the data as integer timestamps.')

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if args:
        parser.print_help()
        sys.exit(1)

    if options.timestamps:
        running_timestamps(*args, strict=options.strict)
    else:
        running_range(*args, strict=options.strict)


if __name__ == '__main__':
    main(sys.argv[1:])

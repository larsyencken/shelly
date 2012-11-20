#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  groupby
#  shelly
#

"""
Group the input by the given key. Useful before a reduce step in
a map-sort-reduce pipeline.
"""

import sys
import optparse
import itertools


def group_lines(field, delimiter=' ', istream=sys.stdin, ostream=sys.stdout,
        unbuffered=False, pop_key=False):
    flush = ostream.flush
    istream = clean_lines(istream)
    popper = key_popper(field, delimiter)
    for key, lines in itertools.groupby(istream,
            key=key_fetcher(field, delimiter)):
        if pop_key:
            lines = itertools.imap(popper, lines)
        print >> ostream, '%s | %s' % (key, ' | '.join(lines).replace('\n',
            ''))
        if unbuffered:
            flush()


def clean_lines(istream):
    for l in istream:
        yield ' '.join(l.split())


def key_fetcher(field, delimiter):
    "Make a function to extract a key from each line."
    def get_key(l):
        return l.lstrip().split(delimiter)[field]

    return get_key


def key_popper(field, delimiter):
    def popper(l):
        l = l.strip().split(delimiter)
        del l[field]
        return delimiter.join(l)

    return popper


def _create_option_parser():
    usage = \
"""%prog groupby [options]

Group the input lines by the given field."""

    parser = optparse.OptionParser(usage)
    parser.add_option('-f', action='store', dest='field_no', type='int',
            help='The index of the field to use as key [0].', default=0)
    parser.add_option('-d', action='store', dest='delimiter', default=' ',
            help='The delimiter to use [ ].')
    parser.add_option('--pop-key', action='store_true', dest='pop_key',
            help='Strip the repeated key.')
    parser.add_option('-u', action='store_true', dest='unbuffered',
            help="Don't buffer output.")

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if args:
        parser.print_help()
        sys.exit(1)

    try:
        group_lines(options.field_no, delimiter=options.delimiter,
                pop_key=options.pop_key, unbuffered=options.unbuffered)
    except KeyboardInterrupt:
        # user quit manually
        pass
    except IOError:
        # often happens with broken pipes
        pass


if __name__ == '__main__':
    main(sys.argv[1:])

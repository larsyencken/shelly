#!/usr/bin/env python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  shrandom.py
#  shelly
#

"""
Random number generation.
"""

import sys
import optparse
import random


def random_uniform(min_=0, max_=1):
    r = random.random
    while True:
        yield min_ + (max_ - min_) * r()


def random_gaussian(mu=0, sigma=1):
    while True:
        yield random.gauss(mu, sigma)


def stream(it):
    try:
        for x in it:
            print x
    except KeyboardInterrupt:
        pass
    except IOError:
        pass


def _create_option_parser():
    usage = \
"""%prog random [options]

Generate a stream of random numbers."""

    parser = optparse.OptionParser(usage)
    parser.add_option('--gaussian', action='store', dest='gauss_params',
            help='Generate gaussian variables with given (mean,std)')

    return parser


def main(argv):
    parser = _create_option_parser()
    (options, args) = parser.parse_args(argv)

    if args:
        parser.print_help()
        sys.exit(1)

    if options.gauss_params:
        try:
            mu, sigma = map(float, options.gauss_params.split(','))
        except ValueError:
            print >> sys.stderr, \
                    'Please specify in the form --gaussian=mu,sigma'
            sys.exit(1)
        stream(random_gaussian(mu, sigma))
    else:
        stream(random_uniform())


if __name__ == '__main__':
    main(sys.argv[1:])

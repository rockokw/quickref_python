#!/usr/bin/env python2.7

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='General description')

    parser.add_argument('num', type=int,
                        help='required number')

    args = parser.parse_args()
    print args


# ❯ ./main.py -h
# usage: main.py [-h] num
#
# General description
#
# positional arguments:
#   num         required number
#
# optional arguments:
#   -h, --help  show this help message and exit
#
#
# ❯ ./main.py 10
# Namespace(num=10)

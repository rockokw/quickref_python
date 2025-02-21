#!/usr/bin/env python3
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="General description")

    parser.add_argument("num", type=int, help="required number")

    parser.add_argument(
        "--verbose", "-v", action="store_true", help="optional flag"
    )

    args = parser.parse_args()
    print(args)

# > ./argparser.py -h
# usage: main.py [-h] [--verbose] num
#
# General description
#
# positional arguments:
#   num            required number
#
# optional arguments:
#   -h, --help     show this help message and exit
#   --verbose, -v  optional flag
#
# > ./argparser.py 10
# Namespace(num=10, verbose=False)
#
# > ./argparser.py -v 10
# Namespace(num=10, verbose=True)

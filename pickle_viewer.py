#!/usr/bin/env python

'''pickle_viewer.py: view Pickle file data.'''
__author__ = 'Kwame Wright'

import argparse
import pickle
import pprint

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='View contents of pickle file'
    )

    parser.add_argument('pickle',
                        help='pickle file')

    parser.add_argument('--pretty', '-p', action='store_true',
                        help='pretty print')

    args = parser.parse_args()

    with open(args.pickle, 'rb') as f:
        p = pickle.load(f)

    if args.pretty:
        pp = pprint.PrettyPrinter(indent=0)
        pp.pprint(p)

    else:
        print(p)

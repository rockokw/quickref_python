#!/usr/bin/env python3
import argparse
import pickle
import pprint

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="View contents of the specified pickle file"
    )

    parser.add_argument("pickle", help="pickle file")

    parser.add_argument(
        "--pretty", "-p", action="store_true", help="pretty print"
    )

    args = parser.parse_args()

    with open(args.pickle, "rb") as f:
        data = pickle.load(f)

    if args.pretty:
        pp = pprint.PrettyPrinter(indent=2, sort_dicts=False)
        pp.pprint(data)
    else:
        print(data)

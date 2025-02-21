#!/usr/bin/env python3
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="print files to standard output"
    )

    parser.add_argument("files", nargs="+", help="files")

    args = parser.parse_args()
    print(args)

    for filename in args.files:
        with open(filename, "r") as f:
            for line in f:
                print(line, end="")

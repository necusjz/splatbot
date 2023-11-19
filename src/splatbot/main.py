#!/usr/bin/env python
import argparse


def macro(args):
    pass


def start(args):
    pass


def main():
    parser = argparse.ArgumentParser("")
    subparser = parser.add_subparsers(title="Commands", dest="command")

    macro_parser = subparser.add_parser("macro", help="Generate macros representing the actual drawing process.")
    macro_parser.add_argument("-i", help="Path to a 320x120 horizontal image to serve as plaza post.")
    macro_parser.set_defaults(func=macro)

    start_parser = subparser.add_parser("start", help="Start drawing and display the current progress.")
    start_parser.add_argument("-i", help="Path to macros that will run on the Pro Controller.")
    start_parser.set_defaults(func=start)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

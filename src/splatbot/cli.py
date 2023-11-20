#!/usr/bin/env python
import click


@click.group(help="Automate drawing detailed plaza posts in Splatoon.")
def main():
    pass


@main.command(help="Generate macros representing the actual drawing process.")
@click.option(
    "--input", "-i", required=True, metavar="PATH",
    help="Path to a 320x120 horizontal image to serve as plaza post."
)
def macro(args):
    pass


@main.command(help="Start drawing and display the current progress.")
@click.option(
    "--input", "-i", required=True, metavar="PATH",
    help="Path to macros simulate the button order from controller."
)
def start(args):
    pass


if __name__ == "__main__":
    main()

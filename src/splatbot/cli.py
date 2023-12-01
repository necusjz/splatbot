#!/usr/bin/env python
import click

from .macro import generate_macro
from .start import start_plotting


@click.group(help="Automate plotting detailed posts in Splatoon wirelessly.")
def main():
    pass


@main.command(help="Generate the macro represents the actual plotting process.")
@click.option(
    "--input", "-i", required=True, metavar="PATH",
    help="Path to a 320x120 horizontal image to serve as a post."
)
def macro(input):
    generate_macro(input)


@main.command(help="Start plotting the post and display the current progress.")
@click.option(
    "--input", "-i", required=True, metavar="PATH",
    help="Path to the macro that simulates the sequence of buttons."
)
def start(input):
    start_plotting(input)


if __name__ == "__main__":
    main()

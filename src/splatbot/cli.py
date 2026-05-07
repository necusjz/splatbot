#!/usr/bin/env python
import click

from .macro import generate_macro
from .start import start_painting


@click.group(help="Automate painting posts in Splatoon based on BlueZ.")
def main():
    pass


@main.command(help="Generate the macro represents the actual painting process.")
@click.option(
    "--input", "-i", required=True, metavar="PATH",
    help="Path to a 320x120 horizontal image to serve as a post."
)
def macro(input):
    generate_macro(input)


@main.command(help="Wirelessly painting the post on switch console or another window.")
@click.option(
    "--input", "-i", required=True, metavar="PATH",
    help="Path to the macro stands for the button sequence."
)
@click.option(
    "--dry-run", is_flag=True,
    help="Do not paint on switch console directly, but do simulation."
)
def start(input, dry_run):
    start_painting(input, dry_run)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import os

import click

from msf.discoverer import read_discoverer_msf

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


def print_help(ctx):
  click.echo(ctx.get_help())
  ctx.exit()

@click.command()
@click.option('--msf_file', '-i', help='msf file')
@click.option('--output', '-o', help='Output tab')
@click.option('--filter', '-f', help='Filter only High-confidence peptides', is_flag = True, default = False)
@click.pass_context
def read_msf(ctx, msf_file: str, output: str, filter : bool):
  if msf_file is None:
    print_help(ctx)

  basename = os.path.basename(msf_file)
  df = read_discoverer_msf(basename=basename, msf_path=msf_file)
  if filter:
    df = df[df['Confidence Level'] == 'High']

  df.to_csv(output, sep="\t", index=True, na_rep='NULL')

def main():
    read_msf()


if __name__ == "__main__":
    main()

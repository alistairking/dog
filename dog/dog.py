#!/usr/bin/env python3
import argparse
import os
from smart_open import open
import shutil
import sys

def main():
    parser = argparse.ArgumentParser(description="""
    Reads from a file (or files) and writes its contents to stdout. Supports
    any compression/transport that smart-open supports.
    """)

    parser.add_argument('files', nargs='*', help='Files to read from')
    opts = vars(parser.parse_args())
    files = opts['files']
    if len(files) == 0:
        files = ["-"]

    for filename in files:
        if filename == "-":
            filename = sys.stdin.buffer
        with open(filename, 'rb') as fh:
            try:
                shutil.copyfileobj(fh, sys.stdout.buffer)
            except BrokenPipeError:
                devnull = os.open(os.devnull, os.O_WRONLY)
                os.dup2(devnull, sys.stdout.fileno())
                sys.exit(1)

if __name__ == '__main__':
    main()

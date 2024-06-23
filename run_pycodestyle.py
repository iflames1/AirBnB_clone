#!/usr/bin/python3

import os
from subprocess import run


def run_pycodestyle():
    for root, _, files in os.walk('.'):
        for filename in files:
            if filename.endswith('.py'):
                filepath = os.path.join(root, filename)
                run(['pycodestyle', filepath])
    print("Done Boss")


if __name__ == '__main__':
    run_pycodestyle()

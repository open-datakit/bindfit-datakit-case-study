#! /usr/bin/env python

import os
import json

from pprint import pprint


invalid_files = []
valid_files = []


def parse():
    cwd = os.getcwd()
    print('\nINVALID JSON FILES:')

    for filename in os.listdir(cwd):
        if filename.endswith(".json"):
            with open(filename) as json_file:
                try:
                    json.load(json_file)
                    valid_files.append(filename)
                except ValueError as error:
                    print("Error at %s,  JSON object issue: %s" % (filename, error, ))
                    invalid_files.append(filename)

    print('\nVALID JSON FILES:')
    pprint(valid_files)

if __name__ == '__main__':
    parse()


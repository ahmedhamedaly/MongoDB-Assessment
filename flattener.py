import json
import sys

# prettifying the output
from util.pretty_json import pretty_json


def flatten(json, flat={}, prefix=None):
    for key, value in json.items():
        prefix_key = (prefix + '.' + key) if prefix else key    # gets the prefix key if object needs flattening

        if type(value) is dict:     # checks if the value of the key is a json object
            flatten(value, flat, prefix_key)    # recurse through the json object
        else:
            flat[prefix_key] = value    # otherwise keep as is

    return flat


# to allow cmd line running while automating tests
def main():

    if not sys.stdin.isatty():      # checks if stdin is empty, otherwise prompts user to try again
        json_file = json.load(sys.stdin)    # takes in input file via stdin

        flat_json = flatten(json_file)

        print(pretty_json(flat_json))   # prettify json (can be used without)

    else:
        print('No file detected, try: cat test_files/test.json | python flattener.py')


if __name__ == "__main__":
    main()

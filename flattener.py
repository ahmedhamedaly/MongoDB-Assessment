import json
import sys

from util.pretty_json import pretty_json


def flatten(json, flat={}, prefix=''):
    for key, value in json.items():
        prefix_key = (prefix + '.' + key) if prefix else key

        if type(value) is dict:
            flatten(value, flat, prefix_key)
        else:
            flat[prefix_key] = value

    return flat


with open('./test_files/test.json', 'r') as f:
    json_file = json.load(f)
    print(pretty_json(flatten(json_file)))
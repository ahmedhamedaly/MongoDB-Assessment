import json


def flatten(json, flat={}, prefix=''):
    for key, value in json.items():
        prefix_key = (prefix + '.' + key) if prefix else key

        if type(value) is dict:
            flatten(value, flat, prefix_key)
        else:
            flat[prefix_key] = value

    return flat


with open('./test_files/sample.json', 'r') as f:
    json_file = json.load(f)
    print(flatten(json_file))
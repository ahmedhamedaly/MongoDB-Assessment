import json


def flatten(json, flat={}, prefix=''):
    for key, value in json.items():
        pf_k = (prefix + '.' + key) if prefix else key

        if type(value) is dict:
            flatten(value, flat, pf_k)
        else:
            flat[pf_k] = value
    
    return flat


with open('./test_files/sample.json', 'r') as f:
    json_file = json.load(f)
    print(flatten(json_file))
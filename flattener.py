import json
import sys

# prettifying the output
from util.pretty_json import pretty_json


def get_input():
    '''
    Retrieves the input file from the user.
        Args:
            N/A

        Raises:
            Exception: No file detected.

        Returns:
            json_object: The json object from the user.
    '''
    if not sys.stdin.isatty():  # checks if stdin is empty, otherwise prompts user to try again
        return json.load(sys.stdin)
    raise Exception('No file detected, try: cat test_files/test.json | python flattener.py') 


def flatten(json, flat={}, prefix=None):
    '''
    Assuming a valid json file input, the method will output a flattened version of the JSON object, with keys as the path to every terminal value in the JSON structure. Output should be valid JSON.

        Args:
            json (json_object): The json file input.
            flat (json_object): The new json object that is flattened.
            prefix (str): String of the prefix of the current json object. 

        Returns:
            flat: Json object flattened.
    '''
    for key, value in json.items():
        prefix_key = (prefix + '.' + key) if prefix else key    # gets the prefix key if object needs flattening

        if type(value) is dict:     # checks if the value of the key is a json object
            flatten(value, flat, prefix_key)    # recurse through the json object
        else:
            flat[prefix_key] = value    # otherwise keep as is

    return flat


# to allow cmd line running while automating tests
def main():
    '''
    Gets the input from the user, turns it to json object and proceeds to flatten it and print a prettified flattened json object.

        Args:
            N/A

        Returns:
            print(flat_json): Prints a prettified flattened json of the input json object.
    '''
    json_file = get_input()    # takes in input file via stdin

    flat_json = flatten(json_file)

    print(pretty_json(flat_json))   # prettify json (can be used without)


if __name__ == "__main__":
    main()

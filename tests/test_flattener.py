import sys
sys.path.append(".")

import unittest
import json
import flattener as flt


class Test_Flatten(unittest.TestCase):
    '''
    A selection of tests designed to test edge cases / possible problems that could arise from the script. Below is the list of files tests:

    - empty.json is an empty json object.
    - flattened.json is an already flattened json object.
    - nested.json has multiple nested objects.
    - no_object.json has an empty object in the main json object
    - sample.json is the sample question provided.

        Args:
            unittest: The test library I decided to use.

        Raises:
            Exception: Expected was different to actual

        Returns:
            N/A
    '''
    def test_empty(self):
        expected = {}
        actual = compute_actual('empty.json')
        
        print('\nTesting Empty json -> Flatten')
        print(f'Expected: {expected}\nActual: {actual}\n')
        self.assertEqual(expected, actual, 'Expected is different than the actual')


    def test_flattened(self):
        expected = {"a":1,"b":True,"c.d":3,"c.e":"test"}
        actual = compute_actual('flattened.json')
        
        print('\nTesting Flattened json -> Flatten')
        print(f'Expected: {expected}\nActual: {actual}\n')
        self.assertEqual(expected, actual, 'Expected is different than the actual')


    def test_nested(self):
        expected = {'a': 1, 'b': True, 'c.d': 3, 'c.e': 'test', 'c.f.g': False, 'c.f.h': 2.1, 'c.f.i.j': 'hi', 'c.f.i.k': 4.9}
        actual = compute_actual('nested.json')
        
        print('\nTesting Nested json -> Flatten')
        print(f'Expected: {expected}\nActual: {actual}\n')
        self.assertEqual(expected, actual, 'Expected is different than the actual')


    def test_no_object(self):
        expected = {"a": 1, "b": True}
        actual = compute_actual('no_object.json')
        
        print('\nTesting No Object json -> Flatten')
        print(f'Expected: {expected}\nActual: {actual}\n')
        self.assertEqual(expected, actual, 'Expected is different than the actual')


    def test_sample(self):
        expected = {"a":1,"b":True,"c.d":3,"c.e":"test"}
        actual = compute_actual('sample.json')
        
        print('\nTesting Sample json -> Flatten')
        print(f'Expected: {expected}\nActual: {actual}\n')
        self.assertEqual(expected, actual, 'Expected is different than the actual')


def compute_actual(file_name):
    '''
    Computes the actual flattened version of the json file name inputted.

        Args:
            file_name (str): The name of file to open and flatten.

        Returns:
            json_object: Flattened version of the input json file name.
    '''
    with open(f'./test_files/{file_name}') as f:
        unflattened = json.load(f)
    
    return flt.flatten(unflattened, {}, None)


if __name__ == "__main__":
    unittest.main()
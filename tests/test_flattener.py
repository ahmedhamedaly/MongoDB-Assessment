import sys
sys.path.append(".")

import unittest
import json
import flattener as flt


class Test_Flatten(unittest.TestCase):

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
    with open(f'./test_files/{file_name}') as f:
        unflattened = json.load(f)
    
    return flt.flatten(unflattened, {}, None)


if __name__ == "__main__":
    unittest.main()
import sys
sys.path.append(".")

import unittest
import json
import flattener

class Test_Flatten(unittest.TestCase):

    def test_empty(self):
        with open('./test_files/test.json') as f:
            expected = json.load(f)
        # actual = json.load(open('./test_files/test.json'))
        # x = flattener.flatten(actual)
        # print(x)

    def test_flattened(self):
        expected = {}
    
    def test_sample(self):
        expected = {}

if __name__ == "__main__":
    unittest.main()
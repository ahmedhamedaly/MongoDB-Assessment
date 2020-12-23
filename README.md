# MongoDB Assessment

## Problem Description

Write a program that takes a JSON object as input and outputs a flattened version of the JSON object, with keys as the path to every terminal value in the JSON structure. Output should be valid JSON.

For example, consider the following JSON object:

``` json
{
    "a": 1,
    "b": true,
    "c": {
        "d": 3,
        "e": "test"
    }
}
```

In this example the path to the terminal value 1 is "a" and the path to the terminal value 3 is "c.d".

The output for the above object would be:

``` json
{
    "a": 1,
    "b": true,
    "c.d": 3,
    "c.e": "test"
}
```

## Assumptions

* The input you receive will be a JSON object
* All keys named in the original object will be simple strings without ‘.’ characters
* The input JSON will not contain arrays
* You may use a library to parse JSON from a string to an object
* Command line should correspond to linux conventions, eg using pipes `cat test.json | mycode`
* Your code will be judged on correctness and code quality, but you do not need to focus on performance optimizations
* Please add tests to validate that your code works correctly.

## Prerequisites

* Python 3.6 >=

## Usage

To pass the json file through command line to the python script, we will use pipes. A pipe is a form of redirection in Unix that transfers a standard input to some other destination. In this example we are redirecting the input file to the python script.

To run using your own json file, replace [input_file] with the location of your json file.

``` shell
cat [input_file] | python flattener.py
```

I have also provided some test files in the `test_files` directory which can be used to test the script.

``` shell
cat test_files/sample.json | python flattener.py
```

## Tests

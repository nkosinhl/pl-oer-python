import unittest, math, random, json, pltest
import getopt, sys, os, stat, subprocess
from unittest.mock import patch
from pltest import name, points
from student_code import student_code
from contextlib import redirect_stdout

def test_with_input(input):
    with open('outfile', 'w') as out:
        with redirect_stdout(out):
            with patch('builtins.input', return_value=str(input)):
                student_code()
    with open('outfile', 'r') as inf:
         return inf.read().strip()

class Test(unittest.TestCase):
    @points(1)
    @name('Checking that it works for 2')
    def test_two(self):
        contents = test_with_input(2)
        self.assertEqual(contents, '-18')

    @points(1)
    @name('Checking that it works for 20')
    def test_five(self):
        contents = test_with_input(20)
        self.assertEqual(contents, '0')

    @points(1)
    @name('Checking that it works for a random number')
    def test_ten(self):
        test_in = random.randint(-5,30)
        contents = test_with_input(test_in)
        res = test_in - 20
        self.assertEqual(contents, str(res))


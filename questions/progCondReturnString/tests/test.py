import unittest, math, random, json, pltest
from pltest import name, points
from bin.student import string_indicating_negativity

class Test(unittest.TestCase):
    @points(4)
    @name("Testing values near 0")
    def test_zero(self):
        self.assertEqual(string_indicating_negativity(0), 'number is not negative')
        self.assertEqual(string_indicating_negativity(1), 'number is not negative')
        self.assertEqual(string_indicating_negativity(-1), 'number is negative')
    @points(3)
    @name("Testing random negative numbers")
    def test_negative(self):
        for i in range(10):
            negative_num = random.randint(-10000, -2)
            self.assertEqual(string_indicating_negativity(negative_num), 'number is negative', negative_num)
    @points(3)
    @name("Testing random positive numbers")
    def test_positive(self):
        for i in range(10):
            positive_num = random.randint(2, 10000)
            self.assertEqual(string_indicating_negativity(positive_num), 'number is not negative', positive_num)

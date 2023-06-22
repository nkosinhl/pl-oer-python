import unittest, math, random, json, pltest
from pltest import name, points
from bin.student import posodd_number_filter

class Test(unittest.TestCase):
    @points(1)
    @name("Testing with 1")
    def test_one(self):
        self.assertEquals(posodd_number_filter(1),"Accepted")

    @points(1)
    @name("Testing with -5")
    def test_ten(self):
        self.assertEquals(posodd_number_filter(-5),"Rejected")

    @points(8)
    @name("Testing with random numbers")
    def test_random(self):
        for i in range(100):
            x = random.randint(-1000, 1000)
            if (x % 2 == 1) and (x > 0):
                self.assertEquals(posodd_number_filter(x),"Accepted")
            else:
                self.assertEquals(posodd_number_filter(x),"Rejected")

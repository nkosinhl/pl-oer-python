#CHANGE THIS
from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
import numpy.random
from numpy import isclose
import math
import inspect

#   f( 0 ) - 0.398942 < 1e-6
#   f( pi ) - 0.002869 < 1e-6

class Test(PLTestCase):
    @points(2)
    @name('Check that i was converted properly.')
    def test_0(self):
    
        if not type(self.st.i) == int:
            Feedback.add_feedback('i is suppose to be an int, but it is not.')
            Feedback.set_score(0)
            return

        if not self.st.i == self.ref.i:
            Feedback.add_feedback(f'i was supposed to contain value {self.ref.i} but has value {self.st.i}')
            Feedback.set_score(0)
            return

        Feedback.add_feedback("Variable i converted correctly.")
        Feedback.set_score(2)

    @points(2)
    @name('Check that x was converted properly.')
    def test_1(self):
    
        if not type(self.st.x) == float:
            Feedback.add_feedback('x is suppose to be a float, but it is not.')
            Feedback.set_score(0)
            return

        if not self.st.x == self.ref.x:
            Feedback.add_feedback(f'x was supposed to contain value {self.ref.x} but has value {self.st.x}')
            Feedback.set_score(0)
            return

        Feedback.add_feedback("Variable x converted correctly.")
        Feedback.set_score(2)

    @points(2)
    @name('Check that s was converted properly.')
    def test_2(self):
    
        if not type(self.st.s) == str:
            Feedback.add_feedback('s is suppose to be a str, but it is not.')
            Feedback.set_score(0)
            return

        if not self.st.s == self.ref.s:
            Feedback.add_feedback(f's was supposed to contain value {self.ref.s} but has value {self.st.s}')
            Feedback.set_score(0)
            return

        Feedback.add_feedback("Variable s converted correctly.")
        Feedback.set_score(2)

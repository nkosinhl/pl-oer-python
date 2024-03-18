#CHANGE THIS
from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCase
from code_feedback import Feedback
from functools import wraps
import numpy as np
from numpy import isclose
import random
import math

class Test(PLTestCase):
    total_iters = 10

    @points(1)
    @not_repeated
    @name('Check that longestWord actually exists.')
    def test_0(self):
    
        points = 1
        
        if self.st.longestWord is None:
            Feedback.add_feedback("You did not define longestWord.")
            points = 0
            
        Feedback.set_score(points)
            
    @points(1)
    @name("Check value of longestWord")
    def test_1(self):
        points = 1
        
        words = "I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past, I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain.".split()

        root = random.randint(0,len(words)-9)
        sample = words[root:root+9]
        
        stm = self.st.longestWord(sample)
        rfm = self.ref.longestWord(sample)
        
        if not stm == rfm:
            Feedback.add_feedback(f"longestWord({sample}) returned {stm} instead of {rfm}.")
            points = 0

        Feedback.set_score(points)


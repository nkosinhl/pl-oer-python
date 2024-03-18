#CHANGE THIS
from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps
import inspect

class Test(PLTestCase):
    @points(1)
    @name('Check that f3 is correct.')
    def test_1(self):
        if self.st.f3 == self.ref.f3:
            Feedback.set_score(1)
            Feedback.add_feedback("f3 is correct.")
        else:
            Feedback.add_feedback(f"s was '{self.ref.s}' so f3 should have been '{self.ref.f3}'.")
            Feedback.set_score(0)

    @points(1)
    @name('Check that m3 is correct.')
    def test_2(self):
        if self.st.m3 == self.ref.m3:
            Feedback.set_score(1)
            Feedback.add_feedback("m3 is correct.")
        else:
            Feedback.add_feedback(f"s was '{self.ref.s}' so m3 should have been '{self.ref.m3}'.")
            Feedback.set_score(0)

    @points(1)
    @name('Check that l3 is correct.')
    def test_3(self):
        if self.st.l3 == self.ref.l3:
            Feedback.set_score(1)
            Feedback.add_feedback("l3 is correct.")
        else:
            Feedback.add_feedback(f"s was '{self.ref.s}' so l3 should have been '{self.ref.l3}'.")
            Feedback.set_score(0)

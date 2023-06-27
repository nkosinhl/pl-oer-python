import random
from code_feedback import Feedback
from pl_helpers import name, points
from pl_unit_test import PLTestCase

def check_string(call_string, desired, actual):
    if desired != actual:
        Feedback.add_feedback(f"your {call_string} produced '{actual}' instead of '{desired}'")
        return False
    return True

class Test(PLTestCase):
    @points(1)
    @name("Testing with 1")
    def test_one(self):
        user_val = Feedback.call_user(self.st.posodd_number_filter, 1)
        if check_string("posodd_number_filter(1)", 'Accepted', user_val): 
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name("Testing with -5")
    def test_ten(self):
        user_val = Feedback.call_user(self.st.posodd_number_filter, -5)
        if check_string("posodd_number_filter(-5)", 'Rejected', user_val): 
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(8)
    @name("Testing with random numbers")
    def test_random(self):
        for i in range(100):
            x = random.randint(-1000, 1000)
            expected = "Accepted" if (x % 2 == 1) and (x > 0) else "Rejected"
            user_val = Feedback.call_user(self.st.posodd_number_filter, x)
            if not check_string(f"posodd_number_filter({x})", expected, user_val): 
                Feedback.set_score(0)
                return
        Feedback.set_score(1)

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
    @points(4)
    @name("Testing values near 0")
    def test_zero(self):
        user_val = Feedback.call_user(self.st.string_indicating_negativity, 0)
        correct1 = check_string("string_indicating_negativity(0)",
                                'number is not negative', user_val)

        user_val = Feedback.call_user(self.st.string_indicating_negativity, 1)
        correct2 = check_string("string_indicating_negativity(1)",
                                'number is not negative', user_val)

        user_val = Feedback.call_user(self.st.string_indicating_negativity, -1)
        correct3 = check_string("string_indicating_negativity(-1)",
                                'number is negative', user_val)

        if correct1 and correct2 and correct3:
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)
            
    @points(3)
    @name("Testing random negative numbers")
    def test_negative(self):
        for i in range(10):
            negative_num = random.randint(-10000, -2)
            user_val = Feedback.call_user(self.st.string_indicating_negativity, negative_num)
            if not check_string(f"string_indicating_negativity({negative_num})",
                                         'number is negative', user_val):
                Feedback.set_score(0)
                return
        Feedback.set_score(1)
         
    @points(3)
    @name("Testing random positive numbers")
    def test_positive(self):
        for i in range(10):
            positive_num = random.randint(2, 10000)
            user_val = Feedback.call_user(self.st.string_indicating_negativity, positive_num)
            if not check_string(f"string_indicating_negativity({positive_num})",
                                         'number is not negative', user_val):
                Feedback.set_score(0)
                return
        Feedback.set_score(1)


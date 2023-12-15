import random

from code_feedback import Feedback
from faker import Faker
from pl_helpers import name, points
from pl_unit_test import PLTestCase


class Test(PLTestCase):
    @points(1)
    @name("Testing with a correct key")
    def test_0_yes(self):
        user_val = Feedback.call_user(
            self.st.get_value_if_key, {"hello": "world"}, "hello"
        )
        if user_val == "world":
            Feedback.set_score(1)
        else:
            Feedback.add_feedback("Your function should return the value for the key.")
            Feedback.set_score(0)

    @points(1)
    @name("Testing with an incorrect key")
    def test_1_tf(self):
        user_val = Feedback.call_user(
            self.st.get_value_if_key, {"hello": "world"}, "world"
        )
        if user_val is None:
            Feedback.set_score(1)
        else:
            Feedback.add_feedback(
                "Your function should return None if the key is not found."
            )
            Feedback.set_score(0)

    @points(3)
    @name("Testing with random dictionaries")
    def test_2_random(self):
        fake = Faker()
        points = 1
        for i in range(10):
            data_dict = fake.pydict(nb_elements=70, value_types=[fake.word, int])
            test_key = (
                random.choice(tuple(data_dict.keys()))
                if random.choice((True, False))
                else fake.word()
            )
            if test_key in data_dict:
                result = data_dict[test_key]
            else:
                result = None
            user_val = Feedback.call_user(self.st.get_value_if_key, data_dict, test_key)
            if user_val != result:
                Feedback.add_feedback(f"Expected {repr(result)}, got {repr(user_val)}")
                points = 0
        Feedback.set_score(points)

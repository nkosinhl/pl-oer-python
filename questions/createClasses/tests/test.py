from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCase
from code_feedback import Feedback

def finish(points,message):
    Feedback.add_feedback(message)
    Feedback.set_score(points)
    return

Feedback.finish = finish

class Test(PLTestCase):

    @points(1)
    @not_repeated
    @name('Existence and Type of student_obj')
    def test_0(self):
        st_ans = self.st.student_obj
        ref_ans = self.ref.student_obj
        if st_ans is None:
            Feedback.finish(0, "You did not define student_obj.")
            return
        if type(st_ans).__name__ != type(ref_ans).__name__:
            Feedback.finish(0, f"student_obj is not a Student object.")
            return
        
        Feedback.finish(1, "The type of student_obj is correct.")
        return


    @points(4)
    @name("Property Value of student_obj")
    def test_1(self):
        st_ans = self.st.student_obj
        ref_ans = self.ref.student_obj
        if type(st_ans).__name__ != type(ref_ans).__name__:
            Feedback.finish(0, "student_obj is not a Student object.")
            return
        
        st_dic = vars(st_ans)
        ref_dic = vars(ref_ans)
        
        if len(st_dic.keys()) == 0:
            Feedback.finish(0, "student_obj does not have any properties. Are you creating the Student class correctly?")
            return
        
        points = 0.25
        for key in ref_dic.keys(): # will loop 3 times
            if key not in st_dic.keys():
                Feedback.finish(points, f"You have a property mismatch. \nThis is your current student_obj information in dictionary form: {st_dic}. \nYou are missing a property {key} in your Student class.")
                return
            if key == "age" and not isinstance(st_dic[key], int):
                Feedback.finish(points, f"Your age property is not an int type.")
                return
            if ref_dic[key] != st_dic[key]:
                if key == "major" and ref_dic[key] == st_dic[key].upper():
                    Feedback.finish(points, "Are you making sure that the major is stored in uppercase letters?")
                else:
                    Feedback.finish(points, f"This is your current student_obj information in dictionary form: {st_dic}. \nA value {st_dic[key]} in your dictionary is incorrect.")
                return
            points += 0.25
        
        if len(st_dic.keys()) > len(ref_dic.keys()):
            points -= 0.25
            Feedback.finish(points, f"This is your current student_obj information in dictionary form: {st_dic}. \nYou are storing more information to your student_obj than what is provided to you. \nMake sure your Student class is correct.")
            return
        
        Feedback.finish(1, "student_obj is correct.")
        return


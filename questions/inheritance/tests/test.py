from pl_helpers import name, points
from pl_unit_test import PLTestCase
from code_feedback import Feedback

def finish(points,message):
    Feedback.add_feedback(message)
    Feedback.set_score(points)
    return

Feedback.finish = finish

class Test(PLTestCase):

    @points(1)
    @name('Existence and Type of it_company_obj')
    def test_0(self):
        st_ans = self.st.it_company_obj
        ref_ans = self.ref.it_company_obj
        if st_ans is None:
            Feedback.finish(0, "You did not define it_company_obj.")
            return
        if type(st_ans).__name__ != type(ref_ans).__name__:
            Feedback.finish(0, f"it_compnay_obj is not a ITCompany object.")
            return
        
        Feedback.finish(1, "The type of it_compnay_obj is correct.")
        return
     
    @points(1)
    @name('Check if it_company_obj is a child of Company class')
    def test_1(self):
        st_ans = self.st.it_company_obj
        ref_ans = self.ref.it_company_obj
        if st_ans is None:
            Feedback.finish(0, "You did not define it_company_obj.")
            return
        if st_ans.__class__.__bases__[0].__name__ != ref_ans.__class__.__bases__[0].__name__:
            Feedback.finish(0, f"it_company_obj is not a child class of {ref_ans.__class__.__bases__[0].__name__}. Did you implement Company class \n Did you inherit the Company class correctly?")
            return
        
        Feedback.finish(1, f"The it_compnay_obj is a child class of {ref_ans.__class__.__bases__[0].__name__}.")
        return

    @points(4)
    @name("Property Value of it_company_obj")
    def test_2(self):
        st_ans = self.st.it_company_obj
        ref_ans = self.ref.it_company_obj
        if type(st_ans).__name__ != type(ref_ans).__name__:
            Feedback.finish(0, "it_company_obj is not a ITCompany object.")
            return
        if st_ans.__class__.__bases__[0].__name__ != ref_ans.__class__.__bases__[0].__name__:
            Feedback.finish(0, f"it_company_obj is not a child class of {ref_ans.__class__.__bases__[0].__name__}. Did you implement Company class \n Did you inherit the Company class correctly?")
            return
        
        st_dic = vars(st_ans)
        ref_dic = vars(ref_ans)
        
        if len(st_dic.keys()) == 0:
            Feedback.finish(0, "it_company_obj does not have any properties. Are you creating the ITCompany class correctly?")
            return
        
        points = 0.25
        for key in ref_dic.keys(): # will loop 3 times
            if key not in st_dic.keys():
                Feedback.finish(points, f"You have a property mismatch. \nThis is your current it_company_obj information in dictionary form: {st_dic}. \nYou are missing a property {key} in your ITCompany class.")
                return
            if key == "name" and not isinstance(st_dic[key], str):
                Feedback.finish(points, f"Your name property is not a string type.")
                return
            if key == "head" and not isinstance(st_dic[key], str):
                Feedback.finish(points, f"Your head property is not a string type.")
                return
            if key == "services" and not isinstance(st_dic[key], list):
                Feedback.finish(points, f"Your services property is not a list type.")
                return
            if ref_dic[key] != st_dic[key]:
                Feedback.finish(points, f"This is your current it_company_obj information in dictionary form: {st_dic}. \nA value {st_dic[key]} in your dictionary is incorrect.")
                return
            points += 0.25
        
        if len(st_dic.keys()) > len(ref_dic.keys()):
            points -= 0.25
            Feedback.finish(points, f"This is your current it_company_obj information in dictionary form: {st_dic}. \nYou are storing more information to your it_company_obj than what is provided to you. \nMake sure your ITcompany class is correct.")
            return
        
        Feedback.finish(1, "it_company_obj is correct.")
        return
    

    @points(2)
    @name('Check get_info method')
    def test_3(self):
        st_ans = self.st.it_company_obj
        ref_ans = self.ref.it_company_obj
        if st_ans is None:
            Feedback.finish(0, "You did not define it_company_obj.")
            return
        
        if st_ans.__class__.__bases__[0].__name__ != ref_ans.__class__.__bases__[0].__name__:
            Feedback.finish(0, f"it_company_obj is not a child class of {ref_ans.__class__.__bases__[0].__name__}. Did you implement Company class \n Did you inherit the Company class correctly?")
            return
        # student function get_info
        
        info_ref = self.ref.it_company_obj.get_info()
        try:
            info_st = Feedback.call_user(self.st.it_company_obj.get_info)
        except AttributeError:
            Feedback.finish(0, "Did you define get_info method in the parent class?")
            return
        
        if info_st is None:
            Feedback.finish(0, "Your get_info method returns None. Make sure it's correctly returning the string!")
            return

        if type(info_st) != str:
            Feedback.finish(0, 'Your get_info is not returning a string type')
            return

        if info_ref!=info_st:
            Feedback.finish(0, 'Are you returning the correct info string as mentioned in the question? Check if you have additional spaces in your info string')
            return
        Feedback.finish(2, "get_info returns correct info string!")
        return
    
    @points(2)
    @name('Check get_services method')
    def test_4(self):
        st_ans = self.st.it_company_obj
        ref_ans = self.ref.it_company_obj
        if st_ans is None:
            Feedback.finish(0, "You did not define it_company_obj.")
            return
        
        if st_ans.__class__.__bases__[0].__name__ != ref_ans.__class__.__bases__[0].__name__:
            Feedback.finish(0, f"it_company_obj is not a child class of {ref_ans.__class__.__bases__[0].__name__}. Did you implement Company class \n Did you inherit the Company class correctly?")
            return
        
        # student function get_info
        
        info_ref = self.ref.it_company_obj.get_services()
        try:
            info_st = Feedback.call_user(self.st.it_company_obj.get_services)
        except AttributeError:
            Feedback.finish(0, "Did you define get_services method in the child class?")
            return
        
        if info_st is None:
            Feedback.finish(0, "Your get_services method returns None. Make sure it's correctly returning a list!")
            return

        if type(info_st) != list:
            Feedback.finish(0, f'Your get_services is not returning a list type but returning a {type(info_st)}')
            return

        if info_ref!=info_st:
            Feedback.finish(0, 'Are you returning the services list correctly using the information from the company_info tuple?')
            return
        Feedback.finish(2, "get_services returns correct info string!")
        return

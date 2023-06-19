import random, copy, json
from pythonHelper import *

templates = [(True, "{0} = {2}", ""), 
             (False, "{2} = {0}", "The left side of an assignment has to be a single variable name"), 
             (True, "{0} = {1} {3} {2}", ""), 
             (True, "{0} = {2} {3} {1}", ""), 
             (False, "{0} {3} {2} = {1}", "The left side of an assignment has to be a single variable name"), 
             (False, "{2} {3} {0} = {1}", "The left side of an assignment has to be a single variable name"), 
             (False, "-{0} = {1} {3} {2}", "The left side of an assignment has to be a single variable name"), 
             (False, "-{0} = {2} {3} {1}", "The left side of an assignment has to be a single variable name"), 
             (True, "{0} = {0}", ""), 
             (True, "{0} = {0} {3} {0}", ""), 
             (True, "{0} {3}= {1}", ""), 
             (True, "{0} {3}= {2}", ""), 
             (True, "{0} {3}= {0}", ""), 
             (True, "{0} {3}= {1} + {2}", ""), 
             (True, "{0} {3}= {1} - {2}", ""), 
             (False, "{0} =/ {1} {3} {2}", "Compound operators have the equal sign on the right"), 
             (False, "{0} =* {1}", "Compound operators have the equal sign on the right"), 
             (False, "{0} =/ {2}", "Compound operators have the equal sign on the right"), 
             (False, "{0} =* {0}", "Compound operators have the equal sign on the right")]

def generate(data):

#    dest_var, src_var
    vars = random.sample(['x', 'y', 'z', 'w', 'q'], 2)
    src_num = random.randint(1, 20)
    operator = random.choice(['-', '+', '*', '/'])
    template = random.choice(templates)

    # Put these two integers into data['params']
    data['params']['code'] = template[1].format(vars[0], vars[1], src_num, operator)
    data['params']['one'] = "Valid" if template[0] else "Invalid"
    data['params']['two'] = "Invalid" if template[0] else "Valid"
    data['correct_answers']['feedback'] = template[2]
    
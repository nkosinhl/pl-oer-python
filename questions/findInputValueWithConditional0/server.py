import re
import random, copy, json
from pythonHelper import *

correct_templates = ["{0} < {1}", "{1} > {0}", "{0} <= {1}", "{1} >= {0}", "{0} <= {2}", "{0} >= {2}", "{0} == {2}", "{0} != {1}", "{1} != {0}"]
incorrect_templates = ["{0} > {1}", "{1} < {0}", "{0} >= {1}", "{1} <= {0}", "{0} == {1}", "{1} == {0}", "{0} != {2}"]

def generate(data):

    data['params']['prefix'] = ""
    data['params']['args'] = ""


    x_val = random.randint(-9, 9)
    y_val = random.randint(-9, 9)
    offset = random.randint(1, 9)

    # twice as likely to use y for the conditional
    compare_var = random.choice(['y', 'y', 'x'])
    compare_var_val = (y_val if (compare_var == 'y') else x_val)
    compare_val = compare_var_val + random.randint(1, 3)

    conditional_taken = random.uniform(0, 1) < .63
    template = random.choice(correct_templates if conditional_taken else incorrect_templates)
    condition = template.format(compare_var, compare_val, compare_var_val)

    arith_op = random.choice(['+', '-'])
    result = x_val
    if conditional_taken:
       if arith_op == '+':
          result += offset
       else:
          result -= offset

    ran = random.choice([0, 1, 2])
    if ran == 0 and compare_var == 'x':
        data['params']['code'] = 'x = k\ny = {1}\nif {2}:\n    x {3}= {4}'.format(x_val, y_val, condition, arith_op, offset)
    elif ran == 1 and compare_var == 'y':
        data['params']['code'] = 'x = {0}\ny = k\nif {2}:\n    x {3}= {4}'.format(x_val, y_val, condition, arith_op, offset)
    else:
        #condition = template.format("k", compare_val, compare_var_val) #buggy, sometimes there will be no k this way, which means any answer works sometimes
        condition = ("k " + template.split(" ")[1] + " " + template.split(" ")[2]).format(compare_var, compare_val, compare_var_val)
        data['params']['code'] = 'x = {0}\ny = {1}\nif {2}:\n    x {3}= {4}'.format(x_val, y_val, condition, arith_op, offset)
    #else:
        #condition = template.format(compare_var, compare_val, "k")
        #data['params']['code'] = 'x = {0}\ny = {1}\nif {2}:\n    x {3}= {4}'.format(x_val, y_val, condition, arith_op, offset)
    data['params']['result'] = result
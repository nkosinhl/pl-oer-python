import random, copy, json
from pythonHelper import *

correct_templates = ["{0} < {1}", "{0} > {3}", "{0} <= {1}", "{0} >= {3}", "{0} <= {2}", "{0} >= {2}", "{0} == {2}", "{0} != {3}"]
incorrect_templates = ["{0} > {1}", "{0} < {3}", "{0} >= {1}", "{0} <= {3}", "{0} == {1}", "{0} != {2}"]

def generate_conditional(x_val):
    compare_val = x_val + random.randint(1, 10)
    compare_val2 = x_val - random.randint(1, 10)

    conditional1_taken = random.choice([True, False])
    template = random.choice(correct_templates if conditional1_taken else incorrect_templates)
    condition1 = template.format('x', compare_val, x_val, compare_val2)

    if fractionOfTime(.50):
        op1 = 'x *= 2'
        x_val2 = (x_val * 2) if conditional1_taken else (x_val)
    else:
        offset = random.randint(5, 15)
        op1 = 'x += ' + str(offset)
        x_val2 = (x_val + offset) if conditional1_taken else (x_val)

    return condition1, op1, x_val2, conditional1_taken


def generate(data):

    x_val = random.randint(1, 20)
    condition1, op1, x_val2, taken = generate_conditional(x_val)
    
    if fractionOfTime(.50):
        op2 = 'x *= 2'
        x_val3 = (x_val * 2) if not taken else (x_val2)
    else:
        offset = random.randint(5, 15)
        op2 = 'x += ' + str(offset)
        x_val3 = (x_val + offset) if not taken else (x_val2)

    data['params']['value'] = x_val
    data['params']['code'] = 'if {0}:\n    {1}\nelse:\n    {2}'.format(condition1, op1, op2)
    data['correct_answers']['result'] = x_val3

    
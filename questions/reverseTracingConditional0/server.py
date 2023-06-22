import re
import random, copy, json

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

    data['correct_answers']['line1'] = str(x_val)
    data['correct_answers']['line2'] = str(y_val)
    
    ran = random.choice([0, 1, 2])
    if ran == 0 and compare_var == 'x':
        data['params']['code'] = 'x = k\ny = {1}\nif {2}:\n    x {3}= {4}'.format(x_val, y_val, condition, arith_op, offset)
        data['correct_answers']['line1'] = 'k'
        
    elif ran == 1 and compare_var == 'y':
        data['params']['code'] = 'x = {0}\ny = k\nif {2}:\n    x {3}= {4}'.format(x_val, y_val, condition, arith_op, offset)
        data['correct_answers']['line2'] = 'k'
    else:
        condition = ("k " + template.split(" ")[1] + " " + template.split(" ")[2]).format(compare_var, compare_val, compare_var_val)
        data['params']['code'] = 'x = {0}\ny = {1}\nif {2}:\n    x {3}= {4}'.format(x_val, y_val, condition, arith_op, offset)
        
    data['correct_answers']['line3'] = f'(x {arith_op} {offset}) if {condition} else x'
        
    data['params']['result'] = result

def parse(data):
    try:
        int(data["submitted_answers"]["k"])
    except:
        data["format_errors"]["k"] = "Not a valid integer"

def grade(data):
    k = int(data["submitted_answers"]["k"])
    x = eval(data['correct_answers']['line1'])    
    y = eval(data['correct_answers']['line2'])    
    x = eval(data['correct_answers']['line3'])    
    correct = data['params']['result']
    data["score"] = 1 if (x == correct) else 0
    data["partial_scores"]["result"] = { "score": data["score"] }
        

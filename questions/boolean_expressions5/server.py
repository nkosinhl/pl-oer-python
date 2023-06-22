import random, copy, json
from pythonHelper import *


def generate(data):

    qtype = random.choice(['abs', 'sqrt', 'idiv', 'exp'])
    invert = random.choice([True, False])
    answers = ['True', 'False']

    if qtype == 'abs':
        base_val = random.randint(-100, 100)
        val = random.choice([-base_val, base_val])      # compare val is either the number or it's negative
        correct_abs = abs(base_val) == val
        if (invert and correct_abs) or (not invert and not correct_abs):
            answers = ['False', 'True']
        code = 'abs({0}) {1} {2}'.format(base_val, '!=' if invert else '==', val)                    
    elif qtype == 'sqrt':
        base_val = random.randint(2, 5)
        val = base_val ** 2
        correct_sqrt = random.choice([True, False])
        if (invert and correct_sqrt) or (not invert and not correct_sqrt):
            answers = ['False', 'True']
        code = 'math.sqrt({0}) {1} {2}'.format(val, '!=' if invert else '==', base_val if correct_sqrt else (-base_val))                    
    elif qtype == 'idiv':
        x_val = random.randint(10, 16)
        y_val = random.randint(3, 5)
        result = x_val // y_val
        correct_result = random.choice([True, False])
        if (invert and correct_result) or (not invert and not correct_result):
            answers = ['False', 'True']
        code = '{0} // {1} {2} {3}'.format(x_val, y_val, '!=' if invert else '==', result if correct_result else (result + 1))                    
    else: # qtype == 'exp':
        val = random.randint(1, 6)
        result = val ** 2
        correct_result = random.choice([True, False])
        if (invert and correct_result) or (not invert and not correct_result):
            answers = ['False', 'True']
        if fractionOfTime(.5):
            code = '{0} ** 2 {1} {2}'.format(val, '!=' if invert else '==', result if correct_result else (-result))
        else:
            code = '(-{0}) ** 2 {1} {2}'.format(val, '!=' if invert else '==', result if correct_result else (-result))                    

    # Put these into data['params']
    data['params']['code'] = code
    data['params']['correct'] = answers[0]
    data['params']['incorrect'] = answers[1]
    data['correct_answers']['qtype'] = qtype


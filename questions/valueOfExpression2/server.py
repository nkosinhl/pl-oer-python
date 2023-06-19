import random, copy, json
from pythonHelper import *

def generate(data):

    operators = ['-', '+', '*', '/']
    operator1 = random.choice(operators)
    operator2 = random.choice(operators)

    a = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])                              # no zero to prevent div by zero
    b = random.choice([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # no zero to prevent div by zero
    if fractionOfTime(.5):
       b, a = a, b
    c = random.randint(2, 6)
    expr1 = '{0} {1} {2}'.format(a, operator1, b)

    data['params']['expression'] = 'x = {0}\nx {1}= {2}'.format(expr1, operator2, c)
    data['correct_answers']['result'] = eval('({0}) {1} {2}'.format(expr1, operator2, c))

    
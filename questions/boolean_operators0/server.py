import random, copy, json
from pythonHelper import *

def generate(data):

    operator = random.choice(['and', 'or'])

    # four times as likely to get [True, False] as either [True, True] or [False, False]
    operands = random.choice([[True, True], [True, False], [True, False], [True, False], [True, False], [False, False]])
    random.shuffle(operands)
    correct = (operands[0] and operands[1]) if operator == 'and' else (operands[0] or operands[1])

    # Put these into data['params']
    data['params']['code'] = '{0} {1} {2}'.format(operands[0], operator, operands[1])
    data['params']['correct'] = 'True' if correct else 'False'
    data['params']['incorrect'] = 'False' if correct else 'True'


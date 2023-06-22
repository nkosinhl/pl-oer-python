import random, copy, json
from pythonHelper import *

true_expressions = ["True and True or False", "True and False or True", "False and True or True", "False and False or True", "False or True and True", "True or False and True", "True or False and False", ]
false_expressions = ["False or False and True", "False or True and False", "False and (True or False)", "True and False or False", "False and True or False", "(True or True) and False"]

def generate(data):

    correct = random.choice([True, False])

    # Put these into data['params']
    data['params']['code'] = random.choice(true_expressions if correct else false_expressions)
    data['params']['correct'] = 'True' if correct else 'False'
    data['params']['incorrect'] = 'False' if correct else 'True'


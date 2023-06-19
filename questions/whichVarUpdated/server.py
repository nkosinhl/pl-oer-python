import random, copy, json
from pythonHelper import *

templates = [(True, "{0} = {2}"), 
             (True, "{0} = {1} {3} {2}"), 
             (True, "{0} = {2} {3} {1}"), 
             (True, "{0} {3}= {1}"), 
             (True, "{0} {3}= {2}"), 
             (True, "{0} {3}= {1} + {2}"), 
             (True, "{0} {3}= {1} - {2}")];

def generate(data):

    vars = random.sample(['x', 'y', 'z', 'w', 'q'], 2)
    src_num = random.randint(1, 20)
    operator = random.choice(['-', '+', '*', '/'])
    template = random.choice(templates)

    # Put these two integers into data['params']
    data['params']['code'] = template[1].format(vars[0], vars[1], src_num, operator)
    data['params']['one'] = vars[0]
    data['params']['two'] = vars[1]
    
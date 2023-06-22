import random, copy, json
from pythonHelper import *

correct_templates = ["{0} < {1}", "{1} > {0}"]
incorrect_templates = ["{0} > {1}", "{1} < {0}"]

def generate(data):

    smaller = random.randint(-1000, -6)
    larger = smaller + random.randint(1, 5)
    correct = random.uniform(0, 1) > 0.5

    template = random.choice(correct_templates if correct else incorrect_templates)

    # Put these into data['params']
    data['params']['code'] = template.format(smaller, larger)
    data['params']['correct'] = 'True' if correct else 'False'
    data['params']['incorrect'] = 'False' if correct else 'True'
    data['correct_answers']['template'] = template


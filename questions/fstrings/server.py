import random, copy, json
from pythonHelper import *

def generate(data):
    my_num = randomInt()
    my_animal = randomAnimal()
    my_fruit  = randomFruit()

    
    fruit_as_variable = True # fractionOfTime(0.5)
    if fruit_as_variable: 
        things = ['{my_num}', '{my_fruit}', my_animal]
        other_def = "my_fruit = '" + my_fruit + "'"
    else:
        things = ['{my_num}', '{my_animal}', my_fruit]
        other_def = "my_animal = '" + my_animal + "'"

    random.shuffle(things)
    vars = ["my_num", "my_animal" if not fruit_as_variable else "my_fruit"]
    random.shuffle(vars)

    defs = ["my_num = " + str(my_num), other_def]
    random.shuffle(defs)

    format_string = " ".join(things)
    quote = randomQuote()
    expr = 'f' + quote + format_string + quote

    # Put these into data['params']
    data['params']['def0'] = defs[0]
    data['params']['def1'] = defs[1]
    data['params']['expr'] = expr
    quote = randomQuote()
    data['correct_answers']['result'] = quote + eval(expr) + quote

def grade(data):
    submitted = " ".join(data["submitted_answers"]["result"].split())
    correct = data['correct_answers']['result']
    data["score"] = 1 if stringContentsSameIndependentOfQuoteTypes(submitted, correct) else 0
    data["partial_scores"]["result"] = { "score": data["score"] }

    

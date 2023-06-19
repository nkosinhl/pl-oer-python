import random, copy, json
from pythonHelper import *

def generate(data):

    operators = [' + ', ' - ', ' * ', ' / ', ' // ', ' % ', ' ** ']
    types = ["int", "float", "string", "not a valid expression"]

    exprStr = randomNumber(.75) + random.choice(operators) + randomNumber(.75)
    if fractionOfTime(0.15):
        quote = '"' if fractionOfTime(0.5) else "'"
        exprStr = quote + exprStr + quote
        answer = "string"
    else:
        try:
            x = eval(exprStr)
            if type(x) is int:
                answer = "int"
            elif type(x) is float:
                answer = "float"
            else:
                answer = "not a valid expression"                
                print(type(x))
        except:
            answer = "not a valid expression"                

    # Put these two integers into data['params']
    data['params']['code'] = "x = " + exprStr
    data['params']['one'] = answer

    types.remove(answer)

    data['params']['two'] = types[0]
    data['params']['three'] = types[1]
    data['params']['four'] = types[2]

#    data['correct_answers']['feedback'] = version[2]
    
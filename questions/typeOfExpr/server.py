import random, copy, json

def fractionOfTime(percent):
    return random.random() < percent

# Random integer between -100 and 100 (inclusive)
def randomInt():
    return str(random.randint(-100, 100))

# Random float between -100.99 and 100.99 (inclusive)
def randomFloat():
    value = random.randint(-100, 100)    
    return str(value) + '.' + str(random.randint(0, 99))

# Randomly generate an int or a float (based on the above)
def randomNumber(percentage = 0.5):
    return randomInt() if fractionOfTime(percentage) else randomFloat()

def randomQuote():
    return '"' if fractionOfTime(0.5) else "'"


def generate(data):

    operators = [' + ', ' - ', ' * ', ' / ', ' // ', ' % ', ' ** ']
    types = ["int", "float", "string", "not a valid expression"]

    exprStr = randomNumber(.75) + random.choice(operators) + randomNumber(.75)
    if fractionOfTime(0.15):
        quote = randomQuote()
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
    
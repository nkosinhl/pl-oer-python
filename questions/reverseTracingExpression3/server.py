import random, copy, json

templates = [("{0} + {1} * {2}", "Remember that multiplication has precedence over addition"),
("{0} - {1} * {2}", "Remember that multiplication has precedence over subtraction"),
("{0} + {1} // {2}", "Remember that division has precedence over addition"),   
("{0} - {1} // {2}", "Remember that division has precedence over subtraction"),
("{0} + {1} % {2}", "Remember that the modulo operator has precedence over addition"),   
("{0} - {1} % {2}", "Remember that the modulo has precedence over subtraction"),
("{0} + {1} ** {2}", "Remember that the exponent operator has precedence over addition"),   
("{0} - {1} ** {2}", "Remember that the exponent operator precedence over subtraction")]

def single_digit_number():
    while True:
        a = random.randint(-9, 9)   # don't want second number to be 1
        if not -1 <= a <= 1:
            return a

def generate(data):

    data['params']['prefix'] = ""
    data['params']['args'] = ""

    template = random.choice(templates)
    version = random.choice([0, 1, 2])
    
    a = single_digit_number()
    b = single_digit_number()
    if 'exponent' in template[1] and version == 1 and b < 0:
        b = -b
    c = random.randint(2, 4)
    expr_str = template[0].format(a, b, c)

    if version == 0:
        expr_strDisplay = template[0].format("y", b, c)
        missing_input = a
    elif version == 1:
        expr_strDisplay = template[0].format(a, "y", c)
        missing_input = b
    else:
        expr_strDisplay = template[0].format(a, b, "y")
        missing_input = c

    data['params']['expression'] = expr_strDisplay
    data['params']['result'] = eval(expr_str)
    extra_feedback = " and unary minus of left operand" if ((b < 0) and '**' in expr_str) else ''
    data['correct_answers']['feedback'] = '{} is one correct answer. There may be others.<br>'.format(missing_input) + template[1] + extra_feedback + '.'

def parse(data):
    try:
        int(data["submitted_answers"]["y"])
    except:
        data["format_errors"]["y"] = "Not a valid integer"


def grade(data):
    y = int(data["submitted_answers"]["y"])
    x = eval(data['params']['expression'])    
    correct = data['params']['result']
    data["score"] = 1 if (x == correct) else 0
    data["partial_scores"]["result"] = { "score": data["score"] }
    
    
    
    

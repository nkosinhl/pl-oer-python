import random, copy, json

int_templates = ["{0} < {1} < {2}", "{0} <= {1} < {2}", "{0} < {1} <= {2}", "{0} <= {1} <= {2}",
             "({1} < {0}) or ({2} < {1})",   "({1} <= {0}) or ({2} < {1})",
             "({1} <= {0}) or ({2} <= {1})", "({1} < {0}) or ({2} <= {1})"]

float_templates = ["{0} < {1} < {2}", "({1} < {0}) or ({2} < {1})"]

def generate(data):

    name = random.choice(['val', 'value', 'candidate_val', 'input_val', 'sensor_value'])
    qtype = random.choice(['int', 'float'])
    edge = random.choice(['upper', 'lower'])

    if qtype == 'int':
        number = random.randint(0, 1000)
        edge_offset = random.randint(-2, 2)
        width = random.randint(6, 200)
        template = random.choice(int_templates)
    else: # qtype == 'float'
        number = round(random.uniform(0, 1000), 2)
        edge_offset = round(random.uniform(-2, 2), 2)
        width = round(random.uniform(6, 200), 2)
        template = random.choice(float_templates)

    if edge == 'upper':
        upper = number + edge_offset
        lower = upper - width
    else: # edge == 'lower':
        lower = number + edge_offset
        upper = lower + width
        
    answer = eval(template.format(lower, number, upper))
    code = template.format(lower, name, upper)                    

    # Put these into data['params']
    data['params']['name'] = name
    data['params']['value'] = number
    data['params']['code'] = code
    data['params']['correct'] = 'True' if answer else 'False'
    data['params']['incorrect'] = 'True' if not answer else 'False'
    data['params']['template'] = template
    data['params']['qtype'] = qtype
    data['params']['edge'] = edge


import random, copy, json

types = ["list", "set", "dictionary"]
versions = [("list", "Lists are specified using square brackets <code>[]</code>  with each element separated by a comma."),
            ("set",  "Sets are specified using curly braces <code>{}</code> with each element separated by a comma."),
            ("dictionary", "Dictionaries are specified using curly braces <code>{}</code> with each key value pair separated by a comma and the key and value separated by a colon <code>:</code>.")]


def generate(data):

    numbers = random.sample(range(-50, 50), random.randint(1, 5))
    version, feedback = random.choice(versions)
    
    if version == 'list':
       code = '[{0}]'.format(', '.join(map(str, numbers)))
    elif version == 'set':
       code = '{' + ', '.join(map(str, numbers)) + '}'
    else: # version == 'dictionary'
       code = '{' + ', '.join(map(lambda x: '{0}: {1}'.format(x, random.randint(-50, 50)), numbers)) + '}'
     

    # Put these two integers into data['params']
    data['params']['code'] = code

    data['params']['one'] = version
    data['params']['two'] = types[0] if version != types[0] else types[1]
    data['params']['three'] = types[2] if version != types[2] else types[1]

    # Put the sum into data['correct_answers']
    data['correct_answers']['feedback'] = feedback
    
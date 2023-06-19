import random, copy, json

templates = [('Written', "{0} = {2}"),
             ('Written', "{0} = {1}"), 
             ('Written', "{0} = {1} {3} {2}"), 
             ('Written', "{0} = {2} {3} {1}"), 
             ('Both', "{0} {3}= {1}"), 
             ('Both', "{0} {3}= {2}"), 
             ('Both', "{0} = {0} {3} {1}"), 
             ('Both', "{0} {3}= {1} + {2}"), 
             ('Both', "{0} {3}= {1} - {2}"),
             ('Read', "{1} = {0}"), 
             ('Read', "{1} {3}= {0}"), 
             ('Read', "{1} {3}= {0} + {2}"), 
             ('Read', "{1} = {0} {3} {2}"),
];

def generate(data):

    other_var = random.choice(['y', 'z', 'w', 'q'])
    src_num = random.randint(1, 20)
    operator = random.choice(['-', '+', '*', '/'])
    template = random.choice(templates)

    answers = ['Read', 'Written', 'Both']
    answers.remove(template[0])

    # Put these two integers into data['params']
    data['params']['code'] = template[1].format('x', other_var, src_num, operator)
    data['params']['one'] = template[0]
    data['params']['two'] = answers[0]
    data['params']['three'] = answers[1]
    
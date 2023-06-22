import random, copy, json

def generate(data):

    initial_list_length = random.randint(3, 7)
    listname = random.choice(['favorite_numbers', 'positions', 'deltas', 'gains', 'yields'])
    mylist = random.sample(range(-20, 21), initial_list_length)

    qtype = random.choice(['append', 'insertion', 'delete', 'pop', 'modification'])
    if qtype == 'append':
       statement = '{0}.append({1})'.format(listname, random.randint(21, 25))
       result = initial_list_length + 1
       feedback = 'The <code>append()</code> function adds a new element to a list making it one element longer.'
    elif qtype == 'insertion':
       statement = '{0}.insert({2}, {1})'.format(listname, random.randint(21, 25), random.randint(0, initial_list_length-1))
       result = initial_list_length + 1
       feedback = 'The <code>insert()</code> function adds a new element at a specific position in a list making it one element longer.'
    elif qtype == 'modification':
       statement = '{0}[{2}] = {1}'.format(listname, random.randint(21, 25), random.randint(0, initial_list_length-1))
       result = initial_list_length
       feedback = "A list modification like the above changes an element in place so the list doesn't change length."
    elif qtype == 'delete':
       statement = '{0}.remove({1})'.format(listname, mylist[random.randint(0, initial_list_length-1)])
       result = initial_list_length - 1
       feedback = 'The <code>remove()</code> function removes the first instance of a specified value from the list, making it one element shorter if the specified value is present.'
    elif qtype == 'pop':
       statement = '{0}.pop({1})'.format(listname, random.randint(0, initial_list_length-1))
       result = initial_list_length - 1
       feedback = 'The <code>pop()</code> function removes the element at the specified index, making the list one element shorter.'


    # Put these into data['params']
    data['params']['code'] = '{0} = {1}\n{2}\nx = len({0})'.format(listname, mylist, statement)
    data['correct_answers']['result'] = result
    data['correct_answers']['feedback'] = feedback

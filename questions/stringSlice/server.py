import random, copy

def generate(data):
    data['params']['names_for_user'] = [
    {'name': 's', 'description': 'A random 9-character string', 'type':'string'}]
    data['params']['names_from_user'] = [
        {'name': 'f3', 'description': 'The first three characters of s', 'type': 'string'},
        {'name': 'm3', 'description': 'The middle three characters of s', 'type': 'string'},
        {'name': 'l3', 'description': 'The last three characters of s', 'type': 'string'}
    ]

import random, copy

def generate(data):
    data['params']['names_for_user'] = [
            {'name':'i', 'description': 'A value that is <b>not</b> an integer.' },
            {'name':'x', 'description': 'A value that is <b>not</b> a float.' },
            {'name':'s', 'description': 'A value that is <b>not</b> a string.' },

            ]
    data['params']['names_from_user'] = [
            {'name':'i', 'description': 'The original value of i converted to an integer.' },
            {'name':'x', 'description': 'The orignal value of x converted to a float.' },
            {'name':'s', 'description': 'The orignal value of s converted to a string.' },
    ]

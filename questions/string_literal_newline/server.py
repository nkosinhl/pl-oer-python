import random, copy, json
from pythonHelper import *

def generate(data):

    text = "\n".join(randomFruit(3))
    answer = '\\n'.join(text.split('\n'))
    quote = randomQuote()

    # Put these into data['params']
    data['params']['text'] = text
    data['correct_answers']['result'] = quote + answer + quote

def grade(data):
    submitted = data["submitted_answers"]["result"]
    correct = data['correct_answers']['result']
    data["score"] = 1 if stringContentsSameIndependentOfQuoteTypes(submitted, correct) else 0
    data["partial_scores"]["result"] = { "score": data["score"] }

    
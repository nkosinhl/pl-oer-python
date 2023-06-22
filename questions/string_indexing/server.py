import random, copy, json
from pythonHelper import *

def generate(data):

    randstr = randomString(5)
    strlen = len(randstr) - 2
    index = random.randint(0, strlen-1)
    text = randstr + '[' + str(index) + ']'

    # Put these into data['params']
    data['params']['text'] = text
    quote = randomQuote()
    data['correct_answers']['result'] = quote + eval(text) + quote

def grade(data):
    submitted = data["submitted_answers"]["result"]
    correct = data['correct_answers']['result']
    data["score"] = 1 if stringContentsSameIndependentOfQuoteTypes(submitted, correct) else 0
    data["partial_scores"]["result"] = { "score": data["score"] }

    
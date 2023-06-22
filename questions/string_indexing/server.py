import random, copy, json

def fractionOfTime(percent):
    return random.random() < percent

def randomQuote():
    return '"' if fractionOfTime(0.5) else "'"

# Random string containing characters
def randomString(baselength = 0):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    random.shuffle(letters)
    quote = '"' if fractionOfTime(0.5) else "'"
    return quote + "".join(letters[:random.randint(baselength+1, baselength+7)]) + quote

def stringContentsSameIndependentOfQuoteTypes(submitted, correct):
    quotes = ['"', "'"]
    if len(submitted) == 0:
        return False
    if submitted[0] not in quotes:
        return False
    if submitted[0] != submitted[-1]:
        return False
    if submitted[1:-1] != correct[1:-1]:
        return False
    return True

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

    
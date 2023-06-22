import random, copy, json

def fractionOfTime(percent):
    return random.random() < percent

def randomQuote():
    return '"' if fractionOfTime(0.5) else "'"

def randomFruit(k = 1):
    fruits = ["Apple", "Akee", "Apricot", "Avocado", "Banana", "Bilberry", "Blackberry", "Blackcurrant", "Blueberry", "Boysenberry", "Currant", "Cherry", "Cloudberry", "Coconut", "Cranberry", "Cucumber", "Damson", "Date", "Durian", "Elderberry", "Feijoa", "Fig", "Gooseberry", "Grape", "Raisin", "Grapefruit", "Guava", "Honeyberry", "Huckleberry", "Jabuticaba", "Jackfruit", "Jambul", "Jostaberry", "Jujube", "Kiwifruit", "Kumquat", "Lemon", "Lime", "Loquat", "Longan", "Lychee", "Mango", "Mangosteen", "Marionberry", "Melon", "Cantaloupe", "Honeydew", "Watermelon", "Mulberry", "Nectarine", "Nance", "Orange", "Clementine", "Mandarine", "Tangerine", "Papaya", "Passionfruit", "Peach", "Pear", "Persimmon", "Plantain", "Plum", "Pineapple", "Pineberry", "Pomegranate", "Pomelo", "Quince", "Raspberry", "Salmonberry", "Redcurrant", "Salak", "Satsuma", "Soursop", "Strawberry", "Tamarillo", "Tamarind", "Yuzu"]
    selection = random.sample(fruits, k)
    return selection[0] if k == 1 else selection

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

    

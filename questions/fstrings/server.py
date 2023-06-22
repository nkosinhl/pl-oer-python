import random, copy, json

def fractionOfTime(percent):
    return random.random() < percent

def randomQuote():
    return '"' if fractionOfTime(0.5) else "'"

# Random integer between -100 and 100 (inclusive)
def randomInt():
    return str(random.randint(-100, 100))

def randomAnimal(k = 1):
    animals = ['aardvark', 'alligator', 'crocodile', 'alpaca', 'ant', 'antelope', 'ape', 'armadillo', 'donkey', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'bee', 'beetle', 'buffalo', 'butterfly', 'camel', 'carabao', 'caribou', 'cat', 'cattle', 'cheetah', 'chimpanzee', 'chinchilla', 'cicada', 'clam', 'cockroach', 'cod', 'coyote', 'crab', 'cricket', 'crow', 'raven', 'deer', 'dinosaur', 'dog', 'dolphin', 'porpoise', 'duck', 'eagle', 'echidna', 'eel', 'elephant', 'elk', 'ferret', 'fish', 'fly', 'fox', 'frog', 'toad', 'gerbil', 'giraffe', 'gnat', 'wildebeest', 'goat', 'goldfish', 'goose', 'gorilla', 'grasshopper', 'hamster', 'hare', 'hedgehog', 'herring', 'hippopotamus', 'hornet', 'horse', 'hound', 'hyena', 'impala', 'insect', 'jackal', 'jellyfish', 'kangaroo', 'wallaby', 'koala', 'leopard', 'lion', 'lizard', 'llama', 'locust', 'louse', 'macaw', 'mallard', 'mammoth', 'manatee', 'marten', 'mink', 'minnow', 'mole', 'monkey', 'moose', 'mosquito', 'mouse', 'rat', 'mule', 'muskrat', 'otter', 'ox', 'oyster', 'panda', 'pig', 'hog', 'platypus', 'porcupine', 'pug', 'rabbit', 'raccoon', 'reindeer', 'rhinoceros', 'salmon', 'sardine', 'scorpion', 'seal', 'serval', 'shark', 'sheep', 'skunk', 'snail', 'snake', 'spider', 'squirrel', 'swan', 'termite', 'tiger', 'trout', 'turtle', 'tortoise', 'walrus', 'wasp', 'weasel', 'whale', 'wolf', 'wombat', 'woodchuck', 'worm', 'yak', 'yellowjacket', 'zebra']
    selection = random.sample(animals, k)
    return selection[0] if k == 1 else selection

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
    my_num = randomInt()
    my_animal = randomAnimal()
    my_fruit  = randomFruit()

    
    fruit_as_variable = fractionOfTime(0.5)
    if fruit_as_variable: 
        things = ['{my_num}', '{my_fruit}', my_animal]
        other_def = "my_fruit = '" + my_fruit + "'"
    else:
        things = ['{my_num}', '{my_animal}', my_fruit]
        other_def = "my_animal = '" + my_animal + "'"

    random.shuffle(things)
    vars = ["my_num", "my_animal" if not fruit_as_variable else "my_fruit"]
    random.shuffle(vars)

    defs = ["my_num = " + str(my_num), other_def]
    random.shuffle(defs)

    format_string = " ".join(things)
    quote = randomQuote()
    expr = 'f' + quote + format_string + quote

    # Put these into data['params']
    data['params']['def0'] = defs[0]
    data['params']['def1'] = defs[1]
    data['params']['expr'] = expr
    quote = randomQuote()
    data['correct_answers']['result'] = quote + eval(expr) + quote

def grade(data):
    submitted = " ".join(data["submitted_answers"]["result"].split())
    correct = data['correct_answers']['result']
    data["score"] = 1 if stringContentsSameIndependentOfQuoteTypes(submitted, correct) else 0
    data["partial_scores"]["result"] = { "score": data["score"] }

    

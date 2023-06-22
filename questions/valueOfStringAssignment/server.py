import random, copy, json

templates = [(1, 0, "y = {0}\nx = y\ny = {1}"),
             (2, 0, "x = {0}\ny = x\ny = {1}"), 
             (3, 1, "x = {0}\ny = {1}\nx = y"),
             (4, 1, "x = {0}\ny = {1}\nx = {2}\nx = y"),
             (5, 1, "y = {0}\nx = {1}\ny = x"), 
             (6, 1, "y = {0}\ny = {1}\nx = y\ny = {2}"), 
             (7, 0, "y = {0}\nx = {1}\nx = y"),
             (8, 0, "x = {0}\ny = {1}\ny = x"), 
             (9, 1, "x = {0}\ny = {1}\nx = y\ny = {2}"),
             (10, 1, "y = {0}\nx = {1}\ny = x\ny = {2}"), 
             (11, 0, "y = {0}\nx = {1}\nx = y\ny = {2}"),
             (12, 0, "x = {0}\ny = {1}\ny = x\ny = {2}"), 
             (13, 0, "x = {1}\ny = {0}\nx = y\ny = {2}"),
             (14, 1, "y = {0}\nx = {1}\ny = x\ny = {2}"),
             (15, 0, "x = {0}\ny = x\nx = {1}\nx = y"),
             (16, 0, "y = {0}\nx = y\ny = {1}\ny = x"),
             (17, 1, "x = {0}\ny = {1}\nx = y\ny = x"),
]              

def randomFruit(k = 1):
    fruits = ["Apple", "Akee", "Apricot", "Avocado", "Banana", "Bilberry", "Blackberry", "Blackcurrant", "Blueberry", "Boysenberry", "Currant", "Cherry", "Cloudberry", "Coconut", "Cranberry", "Cucumber", "Damson", "Date", "Durian", "Elderberry", "Feijoa", "Fig", "Gooseberry", "Grape", "Raisin", "Grapefruit", "Guava", "Honeyberry", "Huckleberry", "Jabuticaba", "Jackfruit", "Jambul", "Jostaberry", "Jujube", "Kiwifruit", "Kumquat", "Lemon", "Lime", "Loquat", "Longan", "Lychee", "Mango", "Mangosteen", "Marionberry", "Melon", "Cantaloupe", "Honeydew", "Watermelon", "Mulberry", "Nectarine", "Nance", "Orange", "Clementine", "Mandarine", "Tangerine", "Papaya", "Passionfruit", "Peach", "Pear", "Persimmon", "Plantain", "Plum", "Pineapple", "Pineberry", "Pomegranate", "Pomelo", "Quince", "Raspberry", "Salmonberry", "Redcurrant", "Salak", "Satsuma", "Soursop", "Strawberry", "Tamarillo", "Tamarind", "Yuzu"]
    selection = random.sample(fruits, k)
    return selection[0] if k == 1 else selection

def generate(data):

    values = list(map(lambda x: "'" + x + "'", randomFruit(3)))
    template = random.choice(templates)
    expr_str = template[2].format(values[0], values[1], values[2])

    data['params']['expression'] = expr_str
    data['params']['one'] = values[template[1]]
    data['params']['two'] = values[1 - template[1]]
    data['params']['three'] = values[2]

    data['correct_answers']['template'] = template[0]

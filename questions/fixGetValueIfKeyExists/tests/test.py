import unittest, math, random, json, pltest
from pltest import name, points
from bin.student import get_value_if_key
animals = ['aardvark', 'alligator', 'crocodile', 'alpaca', 'ant', 'antelope', 'ape', 'armadillo', 'donkey', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'bee', 'beetle', 'buffalo', 'butterfly', 'camel', 'carabao', 'caribou', 'cat', 'cattle', 'cheetah', 'chimpanzee', 'chinchilla', 'cicada', 'clam', 'cockroach', 'cod', 'coyote', 'crab', 'cricket', 'crow', 'raven', 'deer', 'dinosaur', 'dog', 'dolphin', 'porpoise', 'duck', 'eagle', 'echidna', 'eel', 'elephant', 'elk', 'ferret', 'fish', 'fly', 'fox', 'frog', 'toad', 'gerbil', 'giraffe', 'gnat', 'wildebeest', 'goat', 'goldfish', 'goose', 'gorilla', 'grasshopper', 'hamster', 'hare', 'hedgehog', 'herring', 'hippopotamus', 'hornet', 'horse', 'hound', 'hyena', 'impala', 'insect', 'jackal', 'jellyfish', 'kangaroo', 'wallaby', 'koala', 'leopard', 'lion', 'lizard', 'llama', 'locust', 'louse', 'macaw', 'mallard', 'mammoth', 'manatee', 'marten', 'mink', 'minnow', 'mole', 'monkey', 'moose', 'mosquito', 'mouse', 'rat', 'mule', 'muskrat', 'otter', 'ox', 'oyster', 'panda', 'pig', 'hog', 'platypus', 'porcupine', 'pug', 'rabbit', 'raccoon', 'reindeer', 'rhinoceros', 'salmon', 'sardine', 'scorpion', 'seal', 'serval', 'shark', 'sheep', 'skunk', 'snail', 'snake', 'spider', 'squirrel', 'swan', 'termite', 'tiger', 'trout', 'turtle', 'tortoise', 'walrus', 'wasp', 'weasel', 'whale', 'wolf', 'wombat', 'woodchuck', 'worm', 'yak', 'yellowjacket', 'zebra']
    
class Test(unittest.TestCase):
    @points(1)
    @name("Testing with a correct key")
    def test_yes(self):
        self.assertEquals(get_value_if_key({ "hello": "world" }, "hello"), "world")

    @points(1)
    @name("Testing with an incorrect key")
    def test_tf(self):
        self.assertEquals(get_value_if_key({ "hello": "world" }, "world"), None)


    @points(3)
    @name("Testing with random dictionaries")
    def test_random(self):
        for i in range(10):
            data_dict = {}
            keys = random.sample(animals, len(animals) // 2)
            for k in keys:
                data_dict[k] = random.randint(5, 10)
            test_key = random.choice(animals)
            if test_key in data_dict:
                result = data_dict[test_key]
            else:
                result = None
            self.assertEquals(get_value_if_key(data_dict, test_key), result)
#!/usr/bin/env python
from random import randint
DICT_NAME = "my-short-nouns.dict"
DICT_LEN = 30089 - 1

def get_random_word (rand_index):
    with open (DICT_NAME) as fin:
        for pi, line in enumerate (fin):
            if pi == rand_index:
                return line[:-1]

# gen random-string with format <word1>-<word2>randint
def gen_random():
    word1 = get_random_word (randint (0, DICT_LEN)).capitalize()
    word2 = get_random_word (randint (0, DICT_LEN))
    return "{0}-{1}-{2}".format (word1, word2, randint (10, 99))
    
if __name__ == "__main__":
    print (gen_random())

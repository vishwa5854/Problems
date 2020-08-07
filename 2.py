import enchant
from itertools import permutations


def checker(words):
    for i in words:
        if us.check("".join(i)):
            print("".join(i))
            break


us = enchant.Dict("en_US")
checker(permutations(input("Enter the word : ")))

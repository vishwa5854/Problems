import enchant
from itertools import permutations
import threading


def checker(words):
    for i in words:
        if us.check("".join(i)):
            print("".join(i))
            break


us = enchant.Dict("en_US")
word = list(permutations(input()))
length = len(word)

length_ = int(length / 5)
t1 = threading.Thread(target=checker(word[:length_]))
t2 = threading.Thread(target=checker(word[length_: 2 * length_]))
t3 = threading.Thread(target=checker(word[2*length_:3*length_]))
t4 = threading.Thread(target=checker(word[3*length_:4*length_]))
t5 = threading.Thread(target=checker(word[4*length_:5*length_]))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

import random
# coint=random.choice(["head","tails"])
# print(coint)

# from random import choice
# coint=choice(["head","tails"])
# print(coint)



# number=random.randint(10,20)
# print(number)

# cards=["jack","king","queen","ace"]
# random.shuffle(cards)
# for card in cards:
#     print(card)
import statistics
print(statistics.mean([100,70]))

import sys
# print("hello, my name is",sys.argv[0])

# try:
#     print("hello, my name is",sys.argv[1])
# except IndexError:
#     print("need more orguments")

if len(sys.argv)<2:
    print("Too few orguments")
elif len(sys.argv)>2:
    print("Too amny orguments")
else:
    print("hello, my name is",sys.argv[1])


if len(sys.argv)<2:
    print("Too few orguments")
for arg in sys.argv:
    print("hello, my name is",arg)
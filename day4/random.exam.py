# random 함수
# import random
from random import *

print(choice(range(1, 7))) # 주사위

# lottery
numbers = list(range(1, 46))
# print(numbers)
lottery = [] #list

for i in range(6):
    #lottery.append(random.choice(numbers))
    lottery.append(choice(numbers))

print(lottery)

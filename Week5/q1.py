import random

def numGen():
    num = 0
    for i in range(0,6):
        num1 = random.randint(0, 9)
        num = num*10 + num1
    return num

print(numGen())
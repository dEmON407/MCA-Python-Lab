import random

str = input("Enter a String")


def stringSelector(str):
    num1 = random.randint(0, len(str)-1)
    print("Selected Random index is: ", num1)
    return str[num1]


print(stringSelector(str))

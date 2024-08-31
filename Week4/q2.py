num = [5, 8, 9, 6, 5]

def compairLastNums(num):
    if num[0] == num[-1]:
        return True
    return False

print(compairLastNums(num))
eve = [1, 2, 3, 4, 5, 6, 7, 8]
odd = [1, 2, 3, 4, 5, 6, 7, 8]

result = []

for num in eve:
    if num % 2 == 0:
        result.append(num)

for num in odd:
    if num % 2 != 0:
        result.append(num)

print(result)

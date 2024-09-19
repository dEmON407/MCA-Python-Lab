num = int(input("Enter the 4 digit number"))


def sum_of_squares(number):
    number_str = str(number)

    num1 = int(number_str[:2])
    num2 = int(number_str[2:])

    result = num1 ** 2 + num2 ** 2

    print(f"The sum of squares of {num1} and {num2} is: {result}")


sum_of_squares(num)

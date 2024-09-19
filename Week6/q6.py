def analyze_string(input_string):
    # Initialize counters
    uppercase_count = 0
    lowercase_count = 0
    alphabet_count = 0
    digit_count = 0

    # Loop through each character in the string
    for char in input_string:
        if char.isupper():
            uppercase_count += 1
            alphabet_count += 1  # Since uppercase letters are alphabets
        elif char.islower():
            lowercase_count += 1
            alphabet_count += 1  # Since lowercase letters are alphabets
        elif char.isdigit():
            digit_count += 1

    # Display the results
    print(f"Number of uppercase characters: {uppercase_count}")
    print(f"Number of lowercase characters: {lowercase_count}")
    print(f"Total number of alphabets: {alphabet_count}")
    print(f"Number of digits: {digit_count}")


# Main program
input_string = input("Enter a string: ")
analyze_string(input_string)

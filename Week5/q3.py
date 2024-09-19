import random
import string


def generate_password(length=10):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Define the character sets
    upper_case_letters = string.ascii_uppercase
    lower_case_letters = string.ascii_lowercase
    digits = string.digits
    special_symbols = string.punctuation

    password1 = [
                   random.choice(upper_case_letters) for _ in range(2)
               ] + [
                   random.choice(digits)
               ] + [
                   random.choice(special_symbols)
               ]

    # Fill the remaining length with random lower case letters
    remaining_length = length - len(password1)
    password1 += [
        random.choice(lower_case_letters + upper_case_letters + digits + special_symbols) for _ in
        range(remaining_length)
    ]

    # Shuffle the resulting password list to avoid predictable patterns
    random.shuffle(password1)

    # Convert the list to a string and return
    return ''.join(password1)


# Generate a random password
password = generate_password(10)
print("Generated Password:", password)

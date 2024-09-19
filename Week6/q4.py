def encrypt(main_string, symbol_string):
    encrypted_string = ""
    for char in main_string:
        encrypted_string += char + symbol_string
    return encrypted_string


# Decryption function
def decrypt(encrypted_string, symbol_string):
    symbol_length = len(symbol_string)
    decrypted_string = ""

    # Step through the encrypted string and remove the symbols
    for i in range(0, len(encrypted_string), symbol_length + 1):
        decrypted_string += encrypted_string[i]

    return decrypted_string


# Main program
main_string = input("Enter the main string: ")
symbol_string = input("Enter the symbol string to embed: ")

# Encrypt the string
encrypted = encrypt(main_string, symbol_string)
print(f"Encrypted string: {encrypted}")

# Decrypt the string
decrypted = decrypt(encrypted, symbol_string)
print(f"Decrypted string: {decrypted}")

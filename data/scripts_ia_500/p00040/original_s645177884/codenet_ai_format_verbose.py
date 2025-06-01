alphabet = 'abcdefghijklmnopqrstuvwxyz'

def encrypt_character(character, multiplier, increment):
    character_index = alphabet.index(character)
    transformed_index = (character_index * multiplier + increment) % 26
    return alphabet[transformed_index]

def find_valid_parameters(encoded_string):
    target_words = ['that', 'this']
    for multiplier in range(1, 26, 2):
        for increment in range(26):
            decrypted_candidate = ''.join(encrypt_character(char, multiplier, increment) for char in 'that')
            if decrypted_candidate in encoded_string:
                return (multiplier, increment)
            decrypted_candidate = ''.join(encrypt_character(char, multiplier, increment) for char in 'this')
            if decrypted_candidate in encoded_string:
                return (multiplier, increment)

number_of_tests = int(input())

for _ in range(number_of_tests):
    encoded_string = input()

    multiplier, increment = find_valid_parameters(encoded_string)

    decrypted_alphabet = ''.join(encrypt_character(char, multiplier, increment) for char in alphabet)

    translation_table = str.maketrans(decrypted_alphabet, alphabet)

    decrypted_string = encoded_string.translate(translation_table)

    print(decrypted_string)
number_of_characters_to_shift = int(input())

original_text = input()

ciphered_text = ''

ascii_value_of_A = ord('A')
ascii_value_of_Z = ord('Z')

for character in original_text:

    shifted_character_ascii = ord(character) + number_of_characters_to_shift

    if shifted_character_ascii > ascii_value_of_Z:
        wrapped_around_ascii = ascii_value_of_A + shifted_character_ascii - ascii_value_of_Z - 1
        ciphered_text += chr(wrapped_around_ascii)
    else:
        ciphered_text += chr(shifted_character_ascii)

print(ciphered_text)
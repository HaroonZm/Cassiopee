shift_amount = int(input())
input_string = input()

UPPERCASE_START = 65
ALPHABET_SIZE = 26

shifted_chars = []

for char in input_string:
    shifted_char_code = (ord(char) + shift_amount - UPPERCASE_START) % ALPHABET_SIZE + UPPERCASE_START
    shifted_chars.append(chr(shifted_char_code))

shifted_string = "".join(shifted_chars)
print(shifted_string)
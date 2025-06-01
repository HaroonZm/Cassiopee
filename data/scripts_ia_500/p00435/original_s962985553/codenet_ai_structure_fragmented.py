def get_alphabet():
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_input():
    return input()

def find_index(char, alphabet):
    return alphabet.index(char)

def shift_index(index, shift, length):
    return (index - shift) % length

def get_shifted_char(char, alphabet, shift):
    index = find_index(char, alphabet)
    new_index = shift_index(index, shift, len(alphabet))
    return alphabet[new_index]

def process_text(text, alphabet, shift):
    shifted_chars = map(lambda x: get_shifted_char(x, alphabet, shift), text)
    return ''.join(shifted_chars)

def main():
    alphabet = get_alphabet()
    text = get_input()
    shifted_text = process_text(text, alphabet, 3)
    print(shifted_text)

main()
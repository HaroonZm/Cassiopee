def get_alphabet():
    return list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def get_input_string():
    return input()

def find_char_index(char, alphabet):
    return alphabet.index(char)

def shift_index(index, shift, length):
    return (index - shift) % length

def get_shifted_char(char, alphabet, shift):
    index = find_char_index(char, alphabet)
    shifted_index = shift_index(index, shift, len(alphabet))
    return alphabet[shifted_index]

def process_string(text, alphabet, shift):
    result_list = []
    for char in text:
        shifted_char = get_shifted_char(char, alphabet, shift)
        result_list.append(shifted_char)
    return result_list

def convert_list_to_string(lst):
    return ''.join(lst)

def main():
    alphabet = get_alphabet()
    text = get_input_string()
    shifted_chars = process_string(text, alphabet, 3)
    result = convert_list_to_string(shifted_chars)
    print(result)

main()
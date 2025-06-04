def get_encode_list():
    return ["00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111",
            "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111",
            "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111",
            "11000", "11001", "11010", "11011", "11100", "11101", "11110", "11111"]

def get_alphabet():
    return list("ABCDEFGHIJKLMNOPQRSTUVWXYZ .,-'?")

def get_decode_list():
    return ["101", "000000", "000011", "10010001", "010001", "000001", "100101", "10011010",
            "0101", "0001", "110", "01001", "10011011", "010000", "0111", "10011000",
            "0110", "00100", "10011001", "10011110", "00101", "111", "10011111", "1000",
            "00110", "00111", "10011100", "10011101", "000010", "10010010", "10010011", "10010000"]

def get_alphabet2():
    return list(" ',-.?ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def get_input_as_list():
    try:
        return list(input())
    except EOFError:
        return None

def char_to_index(sen, alphabet):
    return alphabet.index(sen)

def char_to_encode_code(sen, encode, alphabet):
    idx = char_to_index(sen, alphabet)
    return encode[idx]

def make_encoded_string(sentence, encode, alphabet):
    list1 = []
    for sen in sentence:
        list1.append(char_to_encode_code(sen, encode, alphabet))
    return ''.join(l for l in list1)

def encoded_string_to_list(encoded_str):
    return list(encoded_str)

def process_sentence(sentence, encode, alphabet):
    encoded_str = make_encoded_string(sentence, encode, alphabet)
    return encoded_string_to_list(encoded_str)

def decode_chunk(tmp, decode):
    if tmp in decode:
        return decode.index(tmp)
    return None

def decoded_index_to_char(num, alphabet2):
    return alphabet2[num]

def decode_sentence(encoded_list, decode, alphabet2):
    tmp = ""
    list2 = []
    while encoded_list != []:
        tmp += encoded_list.pop(0)
        num = decode_chunk(tmp, decode)
        if num is not None:
            char = decoded_index_to_char(num, alphabet2)
            list2.append(char)
            tmp = ""
    return list2

def print_decoded(dec_list):
    print(''.join(l for l in dec_list))

def main():
    encode = get_encode_list()
    alphabet = get_alphabet()
    decode = get_decode_list()
    alphabet2 = get_alphabet2()
    while True:
        sentence = get_input_as_list()
        if sentence is None:
            break
        encoded_list = process_sentence(sentence, encode, alphabet)
        dec_list = decode_sentence(encoded_list, decode, alphabet2)
        print_decoded(dec_list)

main()
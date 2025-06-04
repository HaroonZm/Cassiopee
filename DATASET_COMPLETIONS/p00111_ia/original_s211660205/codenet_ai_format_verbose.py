binary_encoding_list = [
    "00000", "00001", "00010", "00011", "00100", "00101", "00110", "00111",
    "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111",
    "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111",
    "11000", "11001", "11010", "11011", "11100", "11101", "11110", "11111"
]

alphabet_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ .,-'?")

variable_length_codes = [
    "101", "000000", "000011", "10010001", "010001", "000001", "100101", "10011010",
    "0101", "0001", "110", "01001", "10011011", "010000", "0111", "10011000",
    "0110", "00100", "10011001", "10011110", "00101", "111", "10011111", "1000",
    "00110", "00111", "10011100", "10011101", "000010", "10010010", "10010011", "10010000"
]

decoded_alphabet_list = list(" ',-.?ABCDEFGHIJKLMNOPQRSTUVWXYZ")

while True:
    try:
        input_sentence = list(input())
    except EOFError:
        break

    encoded_bits_list = []

    for character in input_sentence:
        character_index = alphabet_list.index(character)
        encoded_bits = binary_encoding_list[character_index]
        encoded_bits_list.append(encoded_bits)

    concatenated_encoded_bits = ''.join(encoded_bits_list)
    encoded_bits_stream = list(concatenated_encoded_bits)

    current_code = ""
    decoded_characters = []

    while encoded_bits_stream:
        current_code += encoded_bits_stream.pop(0)
        if current_code in variable_length_codes:
            decoded_index = variable_length_codes.index(current_code)
            decoded_character = decoded_alphabet_list[decoded_index]
            decoded_characters.append(decoded_character)
            current_code = ""

    decoded_sentence = ''.join(decoded_characters)
    print(decoded_sentence)
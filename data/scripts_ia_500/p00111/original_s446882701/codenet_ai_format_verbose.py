alphabet_and_punctuation = [chr(ascii_code) for ascii_code in range(65, 91)] + list(' .,-\'?')

morse_code_to_character = {
    '101': ' ',
    '000000': '\'',
    '000011': ',',
    '10010001': '-',
    '010001': '.',
    '000001': '?',
    '100101': 'A',
    '10011010': 'B',
    '0101': 'C',
    '0001': 'D',
    '110': 'E',
    '01001': 'F',
    '10011011': 'G',
    '010000': 'H',
    '0111': 'I',
    '10011000': 'J',
    '0110': 'K',
    '00100': 'L',
    '10011001': 'M',
    '10011110': 'N',
    '00101': 'O',
    '111': 'P',
    '10011111': 'Q',
    '1000': 'R',
    '00110': 'S',
    '00111': 'T',
    '10011100': 'U',
    '10011101': 'V',
    '000010': 'W',
    '10010010': 'X',
    '10010011': 'Y',
    '10010000': 'Z'
}

while True:

    try:
        input_string = input()
    except EOFError:
        break

    binary_string = ''
    decoded_message = ''

    for character in input_string:
        character_index = alphabet_and_punctuation.index(character)
        binary_code = bin(character_index)[2:].zfill(5)
        binary_string += binary_code

    for bit_index in range(len(binary_string)):
        current_code = binary_string[:bit_index + 1]
        if current_code in morse_code_to_character:
            decoded_message += morse_code_to_character[current_code]
            binary_string = binary_string[bit_index + 1:]
            break

    print(decoded_message)
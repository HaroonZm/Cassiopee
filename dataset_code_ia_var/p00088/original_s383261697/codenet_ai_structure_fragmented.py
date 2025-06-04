import sys
from sys import stdin

def get_encoder():
    return {
        ' ':'101',
        "'":'000000',
        ',':'000011',
        '-':'10010001',
        '.':'010001',
        '?':'000001',
        'A':'100101',
        'B':'10011010',
        'C':'0101',
        'D':'0001',
        'E':'110',
        'F':'01001',
        'G':'10011011',
        'H':'010000',
        'I':'0111',
        'J':'10011000',
        'K':'0110',
        'L':'00100',
        'M':'10011001',
        'N':'10011110',
        'O':'00101',
        'P':'111',
        'Q':'10011111',
        'R':'1000',
        'S':'00110',
        'T':'00111',
        'U':'10011100',
        'V':'10011101',
        'W':'000010',
        'X':'10010010',
        'Y':'10010011',
        'Z':'10010000'
    }

def get_decoder():
    return {
        '00000':'A',
        '00001':'B',
        '00010':'C',
        '00011':'D',
        '00100':'E',
        '00101':'F',
        '00110':'G',
        '00111':'H',
        '01000':'I',
        '01001':'J',
        '01010':'K',
        '01011':'L',
        '01100':'M',
        '01101':'N',
        '01110':'O',
        '01111':'P',
        '10000':'Q',
        '10001':'R',
        '10010':'S',
        '10011':'T',
        '10100':'U',
        '10101':'V',
        '10110':'W',
        '10111':'X',
        '11000':'Y',
        '11001':'Z',
        '11010':' ',
        '11011':'.',
        '11100':',',
        '11101':'-',
        '11110':"'",
        '11111':'?'
    }

def main(args):
    encoder = get_encoder()
    decoder = get_decoder()
    process_input(encoder, decoder)

def process_input(encoder, decoder):
    for line in sys.stdin:
        process_line(line, encoder, decoder)

def process_line(line, encoder, decoder):
    stripped_line = strip_newline(line)
    encoded_string = encode_text(stripped_line, encoder)
    padded_string = pad_encoded_string(encoded_string)
    decoded_string = decode_string(padded_string, decoder)
    print_result(decoded_string)

def strip_newline(line):
    return line.strip('\n')

def encode_text(text, encoder):
    encoded = ''
    for c in text:
        encoded += encode_character(c, encoder)
    return encoded

def encode_character(c, encoder):
    return encoder[c]

def pad_encoded_string(encoded_string):
    remainder = len(encoded_string) % 5
    if remainder != 0:
        padding = get_padding_string(5 - remainder)
        encoded_string += padding
    return encoded_string

def get_padding_string(length):
    return '0' * length

def decode_string(padded_string, decoder):
    result = ''
    while not is_empty(padded_string):
        chunk = get_next_chunk(padded_string)
        result += decode_chunk(chunk, decoder)
        padded_string = remove_chunk(padded_string)
    return result

def is_empty(string):
    return len(string) == 0

def get_next_chunk(s):
    return s[:5]

def remove_chunk(s):
    return s[5:]

def decode_chunk(chunk, decoder):
    return decoder[chunk]

def print_result(res):
    print(res)

if __name__ == '__main__':
    main(sys.argv[1:])
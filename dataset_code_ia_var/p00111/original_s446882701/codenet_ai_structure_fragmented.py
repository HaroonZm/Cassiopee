def get_en_list():
    return [chr(i) for i in range(65, 91)] + list(' .,-\'?')

def get_de_dict():
    return {
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

def char_to_index(char, en_list):
    return en_list.index(char)

def char_to_bin(index):
    return bin(index)[2:]

def bin_string_five_bits(bin_str):
    return bin_str.zfill(5)

def process_char(char, en_list):
    idx = char_to_index(char, en_list)
    bstr = char_to_bin(idx)
    return bin_string_five_bits(bstr)

def process_line_to_binary(s, en_list):
    result = ''
    for x in s:
        result += process_char(x, en_list)
    return result

def try_to_decode_buffer(buffer, de_dict):
    if buffer in de_dict:
        print(de_dict[buffer], end='')
        return True
    return False

def process_binary_message(a, de_dict):
    b = ''
    for i in range(len(a)):
        b += a[i]
        if try_to_decode_buffer(b, de_dict):
            b = ''
    print()

def process_input_line(s, en_list, de_dict):
    a = process_line_to_binary(s, en_list)
    process_binary_message(a, de_dict)

def main():
    en_list = get_en_list()
    de_dict = get_de_dict()
    while True:
        try:
            s = input()
        except:
            break
        process_input_line(s, en_list, de_dict)

main()
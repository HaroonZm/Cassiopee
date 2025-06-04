def get_c2d():
    return {'A':"100101", 'B':"10011010", 'C':"0101", 'D':"0001", 'E':"110", 'F':"01001",
        'G':"10011011", 'H':"010000", 'I':"0111", 'J':"10011000", 'K':"0110", 'L':"00100",
        'M':"10011001", 'N':"10011110", 'O':"00101", 'P':"111", 'Q':"10011111", 'R':"1000",
        'S':"00110", 'T':"00111", 'U':"10011100", 'V':"10011101", 'W':"000010", 'X':"10010010",
        'Y':"10010011", 'Z':"10010000", ' ':"101", "'":"000000", ',':"000011",
        '-':"10010001", '.':"010001", '?':"000001"}

def get_d2c():
    return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '.', ',', '-', "'", '?']

def read_input():
    try:
        return input()
    except EOFError:
        return None

def char_to_code(char, c2d):
    return c2d[char]

def line_to_bits(line, c2d):
    return ''.join(char_to_code(c, c2d) for c in line)

def pad_bits(bits):
    rem = len(bits) % 5
    if rem > 0:
        bits += '0' * (5 - rem)
    return bits

def split_bits(bits):
    return [bits[i:i+5] for i in range(0, len(bits), 5)]

def bits_to_char(bits_group, d2c):
    idx = int(bits_group, 2)
    return d2c[idx]

def bits_groups_to_message(bits_groups, d2c):
    return ''.join(bits_to_char(bg, d2c) for bg in bits_groups)

def process_line(line, c2d, d2c):
    bits = line_to_bits(line, c2d)
    padded = pad_bits(bits)
    groups = split_bits(padded)
    message = bits_groups_to_message(groups, d2c)
    return message

def main():
    c2d = get_c2d()
    d2c = get_d2c()
    while True:
        line = read_input()
        if line is None:
            break
        result = process_line(line, c2d, d2c)
        print(result)

main()
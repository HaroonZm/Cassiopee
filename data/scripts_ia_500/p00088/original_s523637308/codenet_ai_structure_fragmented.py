def get_c2d_mapping():
    return {
        'A': "100101", 'B': "10011010", 'C': "0101", 'D': "0001", 'E': "110", 'F': "01001",
        'G': "10011011", 'H': "010000", 'I': "0111", 'J': "10011000", 'K': "0110",
        'L': "00100", 'M': "10011001", 'N': "10011110", 'O': "00101", 'P': "111",
        'Q': "10011111", 'R': "1000", 'S': "00110", 'T': "00111", 'U': "10011100",
        'V': "10011101", 'W': "000010", 'X': "10010010", 'Y': "10010011", 'Z': "10010000",
        ' ': "101", "'": "000000", ',': "000011", '-': "10010001", '.': "010001", '?': "000001"
    }

def get_d2c_list():
    return [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '.', ',', '-',	'\'', '?'
    ]

def read_input_line():
    try:
        return input()
    except EOFError:
        return None

def convert_char_to_bits(c, mapping):
    return mapping[c]

def concatenate_bits_from_string(s, mapping):
    result = ''
    for ch in s:
        result = concatenate_bits(result, convert_char_to_bits(ch, mapping))
    return result

def concatenate_bits(bits1, bits2):
    return bits1 + bits2

def pad_bits_to_multiple_of_five(bits):
    length = len(bits)
    remainder = length % 5
    if remainder == 0:
        return bits
    else:
        return pad_bits(bits, 5 - remainder)

def pad_bits(bits, count):
    return bits + ('0' * count)

def split_bits_into_chunks(bits, chunk_size):
    chunks = []
    start = 0
    while start < len(bits):
        chunks.append(bits[start:start+chunk_size])
        start += chunk_size
    return chunks

def bits_chunk_to_index(bits_chunk):
    return int(bits_chunk, 2)

def index_to_char(index, d2c):
    return d2c[index]

def decode_bits_to_string(bits, d2c):
    chunks = split_bits_into_chunks(bits, 5)
    result = ''
    for chunk in chunks:
        idx = bits_chunk_to_index(chunk)
        result = concatenate_chars(result, index_to_char(idx, d2c))
    return result

def concatenate_chars(str1, ch):
    return str1 + ch

def process_line(line, c2d, d2c):
    bits = concatenate_bits_from_string(line, c2d)
    padded_bits = pad_bits_to_multiple_of_five(bits)
    decoded = decode_bits_to_string(padded_bits, d2c)
    return decoded

def main():
    c2d = get_c2d_mapping()
    d2c = get_d2c_list()
    while True:
        line = read_input_line()
        if line is None:
            break
        result = process_line(line, c2d, d2c)
        print(result)

main()
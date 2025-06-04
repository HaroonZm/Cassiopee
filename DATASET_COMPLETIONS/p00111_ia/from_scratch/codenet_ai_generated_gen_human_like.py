code_table = {
    'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011', 'E': '00111',
    'F': '00110', 'G': '00101', 'H': '00100', 'I': '01111', 'J': '01110',
    'K': '01101', 'L': '01100', 'M': '01000', 'N': '01001', 'O': '01010',
    'P': '111',    'Q': '11110', 'R': '110',   'S': '10111', 'T': '1010',
    'U': '100',    'V': '10101', 'W': '10000', 'X': '10001', 'Y': '11001',
    'Z': '10100',
    ' ': '0000'
}

inverse_code_table = {v: k for k, v in code_table.items()}

def decode(encoded):
    # First map the input characters to their codes
    # unknown chars are replaced by '?', which is ignored in decoding
    codes = []
    for ch in encoded:
        if ch in code_table:
            codes.append(code_table[ch])
        else:
            # ignore unknown characters
            pass
    bit_stream = ''.join(codes)

    result = []
    i = 0
    n = len(bit_stream)
    while i < n:
        # At each position try to find the longest matching code
        # Since codes have variable length, try slices from longer to shorter
        matched = False

        # The shortest code length is 3, longest is 5
        for length in range(5, 2, -1):
            if i+length <= n:
                segment = bit_stream[i:i+length]
                if segment in inverse_code_table:
                    result.append(inverse_code_table[segment])
                    i += length
                    matched = True
                    break
        if not matched:
            # if no code matched, drop 1 bit (simulates borrowing bits as explained)
            i += 1

    return ''.join(result)

import sys

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    print(decode(line))
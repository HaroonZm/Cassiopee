code_map = {
    'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011', 'E': '00100', 'F': '00101', 'G': '00110', 'H': '00111',
    'I': '01000', 'J': '01001', 'K': '01010', 'L': '01011', 'M': '01100', 'N': '01101', 'O': '01110', 'P': '01111',
    'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011', 'U': '10100', 'V': '10101', 'W': '10110', 'X': '10111',
    'Y': '11000', 'Z': '11001', "'": '11010', '-': '11011', '?': '11100', '.': '11101', ',': '11110', ' ': '11111'
}
rev_map = {v:k for k,v in code_map.items()}

def encode(s):
    s = s.upper()
    bits = ''.join(code_map[c] for c in s)
    return bits

def decode(bits):
    res = []
    idx = 0
    n = len(bits)
    while idx < n:
        for length in range(5,2,-1):
            if idx+length<=n:
                piece = bits[idx:idx+length]
                if piece in rev_map:
                    res.append(rev_map[piece])
                    idx += length
                    break
        else:
            idx +=1
    return ''.join(res)

import sys

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    bits=''.join(code_map[c] for c in line)
    # decode bits greedily, trying 5,4,3 bits
    output=[]
    i=0
    while i<len(bits):
        for l in range(5,2,-1):
            if i+l<=len(bits):
                piece=bits[i:i+l]
                if piece in rev_map:
                    output.append(rev_map[piece])
                    i+=l
                    break
        else:
            i+=1
    print(''.join(output))
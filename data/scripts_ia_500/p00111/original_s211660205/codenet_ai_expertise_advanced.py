encode = [f"{i:05b}" for i in range(32)]
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ .,-'?")
decode = ["101", "000000", "000011", "10010001", "010001", "000001", "100101", "10011010",
          "0101", "0001", "110", "01001", "10011011", "010000", "0111", "10011000",
          "0110", "00100", "10011001", "10011110", "00101", "111", "10011111", "1000",
          "00110", "00111", "10011100", "10011101", "000010", "10010010", "10010011", "10010000"]
alphabet2 = list(" ',-.?ABCDEFGHIJKLMNOPQRSTUVWXYZ")

import sys

encode_map = {c: encode[i] for i, c in enumerate(alphabet)}
decode_map = {code: alphabet2[i] for i, code in enumerate(decode)}

for line in sys.stdin:
    # Convert each character to its 5-bit code and join
    bits = ''.join(encode_map[ch] for ch in line.rstrip('\n'))

    # Decode bits dynamically using a sliding window and a lookup set for efficiency
    decoded_chars = []
    buffer = ''
    decode_keys = set(decode_map.keys())
    idx = 0
    length = len(bits)
    while idx < length:
        buffer += bits[idx]
        idx += 1
        if buffer in decode_keys:
            decoded_chars.append(decode_map[buffer])
            buffer = ''
    print(''.join(decoded_chars))
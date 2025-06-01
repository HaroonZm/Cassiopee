c2d = {
    **dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", [
        "100101", "10011010", "0101", "0001", "110", "01001",
        "10011011", "010000", "0111", "10011000", "0110", "00100",
        "10011001", "10011110", "00101", "111", "10011111", "1000",
        "00110", "00111", "10011100", "10011101", "000010", "10010010",
        "10010011", "10010000"
    ])),
    ' ': "101", "'": "000000", ',': "000011", '-': "10010001",
    '.': "010001", '?': "000001"
}
d2c = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ .,-'?")

import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    bits = ''.join(c2d[ch] for ch in line)
    bits += '0' * (-len(bits) % 5)
    print(''.join(d2c[int(bits[i:i+5], 2)] for i in range(0, len(bits), 5)))
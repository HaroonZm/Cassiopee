digit = [0, 1, 2, 3, 5, 7, 8, 9]

while (n := int(input())) != 0:
    res = ''.join(str(digit[(n // 8**i) % 8]) for i in reversed(range(n.bit_length() // 3 + 1)))
    print(res.lstrip('0') or '0')
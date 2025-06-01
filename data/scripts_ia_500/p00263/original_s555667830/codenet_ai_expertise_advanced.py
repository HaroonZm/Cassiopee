from sys import stdin

BIN = [0] * 32
BIN[1:25] = (1 << i for i in range(23, -1, -1))
BIN[25:] = (0.5 / (2 ** (i - 25)) for i in range(25, 32))

input_iter = iter(stdin.read().splitlines())
Q = int(next(input_iter))

for _ in range(Q):
    bits = format(int(next(input_iter), 16), '032b')
    res = sum(b * int(bit) for b, bit in zip(BIN[1:], bits[1:]))
    print(f"{'-' if bits[0] == '1' else ''}{res}")
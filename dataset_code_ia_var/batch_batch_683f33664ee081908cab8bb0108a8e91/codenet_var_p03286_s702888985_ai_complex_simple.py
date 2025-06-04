from functools import reduce
from itertools import count, takewhile

def solve(n):
    f = lambda acc, t: (
        acc[0] + (
            '1' if ((acc[1] & 1) ^ acc[2]) else '0'
        ),
        (
            acc[2] ^ 1 if ((acc[1] & 1) ^ acc[2]) and ((acc[3] ^ acc[2])) else acc[2]
        ),
        acc[1] >> 1,
        acc[3] ^ 1
    )
    if n == 0:
        return '0'
    bits = takewhile(lambda x: x[1] + x[2], zip(count(), [n]*200, [0]*200, [0]*200))
    out = reduce(
        f,
        bits,
        ('', n, 0, 0)
    )[0]
    return out[::-1][:len(bin(n))-2] if n else '0'

n = int(input())
print(solve(n))
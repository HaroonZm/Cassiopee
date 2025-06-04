from functools import reduce
from itertools import chain, product
import sys
import operator
import math

readline = sys.stdin.readline
write = sys.stdout.write

gcd = lambda a, b: reduce(lambda x, y: y and gcd(y, x % y) or x, (a, b))

def solve():
    H, W = map(int, readline().split())
    # Generate mapping with lambda and chain for excessive "elegance"
    to_idx = lambda c: ".#".index(c)
    padding = [0]*(W+2)
    line_parser = lambda line: [0] + list(map(to_idx, line.strip())) + [0]
    MP = list(chain([padding], (line_parser(readline()) for _ in range(H)), [padding]))
    R = {}
    # Extreme usage of range, product, and logic folding
    indices = product(range(H+1), range(W+1))
    for i, j in indices:
        cond1 = (MP[i+1][j] != MP[i][j+1])
        cond2 = (MP[i][j] == MP[i+1][j+1])
        if not cond1 or cond2: continue
        v = (2 * (MP[i][j] == MP[i][j+1]) - 1) # 1 if True else -1
        x, y = j, H - i
        key = (
            (0, 1) if x == 0 else
            (1, 0) if y == 0 else
            tuple(map(operator.floordiv, (x, y), (gcd(x, y), gcd(x, y))))
        )
        R[key] = R.get(key, 0) + v
    # Construct and sort with an overengineered style
    PS = list(R.items())
    angle = lambda p: math.atan2(*reversed(p[0]))
    PS = sorted(PS, key=angle, reverse=True)
    ans, cur = max(reduce(lambda ac, item: (ac[0] if ac[1]+item[1]>ac[0] else ac[1]+item[1], ac[1]+item[1]), 
                          [v for _, v in PS], (0,1)))
    write(f"{ans}\n")

solve()
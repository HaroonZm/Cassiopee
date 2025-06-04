from math import isqrt
from sys import stdin

def process_queries(queries):
    for a, b in queries:
        prod = a * b
        sq = isqrt(prod)
        ans = (sq << 1) - 1  # sq * 2 - 1
        if a == b:
            ans -= 1
        elif sq * sq == prod:
            ans -= 2
        elif sq * (sq + 1) >= prod:
            ans -= 1
        print(ans)

Q = int(stdin.readline())
queries = [tuple(map(int, stdin.readline().split())) for _ in range(Q)]
process_queries(queries)
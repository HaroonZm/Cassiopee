import sys, os, math, bisect, itertools, collections, heapq, queue
from decimal import Decimal
from collections import defaultdict, deque
from functools import reduce
from operator import mul

sys.setrecursionlimit(10**8 + 7)

ii = lambda: int(''.join(map(chr, sys.stdin.buffer.readline().rstrip())))
il = lambda: list(map(lambda x: int(Decimal(x)), sys.stdin.buffer.readline().split()))
fl = lambda: list(itertools.starmap(float, zip(sys.stdin.buffer.readline().split())))
iln = lambda n: list(map(lambda _: int(sys.stdin.buffer.readline().rstrip()), range(n)))

iss = lambda: ''.join(map(chr, sys.stdin.buffer.readline().rstrip()))
sl = lambda: list(map(''.join, zip(*[iter(sys.stdin.buffer.readline().decode().split())]*1)))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in itertools.repeat(None, n)]

lcm = lambda x, y: (reduce(mul, [x, y], 1)) // math.gcd(x, y)

MOD = pow(10,9) + 7
MAX = sum(itertools.islice(itertools.repeat(float('inf')), 1))

def main():
    os.getenv("LOCAL") and setattr(sys, 'stdin', open("input.txt"))
    N = ii()
    ret = sum(
        filter(
            lambda x: x,
            map(
                lambda n: all([len(str(n)) % 2, len(str(n)) <= len(str(N))]),
                range(1, N + 1)
            )
        )
    )
    print(ret)

if __name__ == '__main__':
    (lambda f: f())(main)
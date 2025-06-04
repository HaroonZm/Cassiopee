import sys
from collections import defaultdict
from typing import List

sys.setrecursionlimit(1 << 25)
INF = float('inf')
EPS = 1e-10
MOD = 10**9 + 7
DD = [(0, -1), (1, 0), (0, 1), (-1, 0)]
DDN = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

def LI() -> List[int]:
    return list(map(int, sys.stdin.readline().split()))

def I() -> int:
    return int(sys.stdin.readline())

def pf(s): 
    print(s, flush=True)

def main():
    n = I()
    a = [LI() for _ in range(n)]
    d = defaultdict(int)
    for x, y, w in a:
        for dx in (0, 1):
            for dy in (0, 1):
                d[(x + dx, y + dy)] += w
    r = max(d.values(), default=0)
    return f'{r} / 1'

if __name__ == "__main__":
    print(main())
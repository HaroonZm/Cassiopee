import os
import sys
from functools import lru_cache
from bisect import bisect_left

def inp():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(inp())

def read_ints():
    return list(map(int, inp().split()))

DEBUG = 'DEBUG' in os.environ
def dprint(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)

def solve(N, V):
    V = sorted(set(V))
    pos = {v: i for i, v in enumerate(V)}
    N = len(V)
    best = 2
    visited = set()
    for i, a in enumerate(V):
        for j in range(i + 1, N):
            if (i, j) in visited:
                continue
            b = V[j]
            d = b - a
            count = 2
            path = [(i, j)]
            k, curr = j, b + d
            while curr in pos:
                nxt = pos[curr]
                path.append((k, nxt))
                k, curr = nxt, curr + d
                count += 1
            for u, v_ in path:
                visited.add((u, v_))
            best = max(best, count)
    return best

def main():
    N = read_int()
    V = read_ints()
    print(solve(N, V))

if __name__ == '__main__':
    main()
from sys import stdin
from typing import List

def solve():
    lines = iter(stdin.readlines())
    while True:
        try:
            N, M = map(int, next(lines).split())
        except StopIteration:
            break
        if N == 0:
            break

        parent = list(range(N + 1))
        rank = [1] * (N + 1)
        diff = [0] * (N + 1)

        def find(x: int) -> int:
            if parent[x] != x:
                orig = parent[x]
                parent[x] = find(parent[x])
                diff[x] += diff[orig]
            return parent[x]

        def union(a: int, b: int, w: int):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            # diff[x]: total diff from x up to root
            rel = w + diff[a] - diff[b]
            if rank[ra] < rank[rb]:
                parent[ra] = rb
                diff[ra] = -rel
            else:
                parent[rb] = ra
                diff[rb] = rel
                if rank[ra] == rank[rb]:
                    rank[ra] += 1

        results = []
        for _ in range(M):
            s = next(lines).split()
            if s[0] == '!':
                a, b, w = map(int, s[1:])
                union(a, b, w)
            else:
                a, b = map(int, s[1:])
                if find(a) == find(b):
                    results.append(str(diff[b] - diff[a]))
                else:
                    results.append('UNKNOWN')
        print('\n'.join(results))

solve()
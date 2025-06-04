from itertools import count, islice, chain, product
from functools import reduce, lru_cache
from operator import itemgetter
from collections import deque
import sys

H, W, K = map(int, sys.stdin.readline().split())
A = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
s = next(((i, a.index("S")) for i, a in enumerate(A) if "S" in a), None)
y, x = s
min_dist = float('inf')
Q = deque([(1, y, x)])

mask = lambda r, c, H, W: all((0 <= r, r < H, 0 <= c, c < W))
neigh = lambda i, j: map(lambda t: (i + t[0], j + t[1]), [(1, 0), (0, 1), (-1, 0), (0, -1)])

visited = set()

while Q:
    c, i, j = Q.popleft()
    min_dist = min(min_dist, i, j, H - i - 1, W - j - 1)
    if c > K: continue
    for h, w in neigh(i, j):
        if mask(h, w, H, W) and A[h][w] == ".":
            if (h, w) in visited: continue
            visited.add((h, w))
            A[h][w] = ","  # obscure marker
            Q.extend([(c + 1, h, w)])

res = 1 + -(min_dist // K)
print(res)
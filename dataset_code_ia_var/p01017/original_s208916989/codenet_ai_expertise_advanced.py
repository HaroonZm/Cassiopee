from sys import stdin
from itertools import product

H, W = map(int, stdin.readline().split())
a_mp = [list(map(int, stdin.readline().split())) for _ in range(H)]
b_mp = [list(map(int, stdin.readline().split())) for _ in range(H)]
h, w = map(int, stdin.readline().split())
c_mp = [list(map(int, stdin.readline().split())) for _ in range(h)]
INF = float('-inf')

c_tuple = tuple(tuple(row) for row in c_mp)

def check(x, y):
    sub_b = tuple(tuple(b_mp[y+dy][x:x+w]) for dy in range(h))
    if sub_b != c_tuple:
        return INF
    return sum(a_mp[y+dy][x+dx] for dy, dx in product(range(h), range(w)))

positions = ((y, x) for y in range(H-h+1) for x in range(W-w+1))
scores = (check(x, y) for y, x in positions)
ans = max(scores, default=INF)
print(ans if ans != INF else "NA")
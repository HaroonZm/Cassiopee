from collections import Counter
from sys import stdin

W, H, T = map(int, stdin.readline().split())
P = int(stdin.readline())
plants = Counter(tuple(map(int, line.split()[:2])) for line in (stdin.readline() for _ in range(P)))

ans = 0
for y in range(H):
    row = list(map(int, stdin.readline().split()))
    for x, v in enumerate(row):
        if v:
            ans += plants.get((x, y), 0)
print(ans)
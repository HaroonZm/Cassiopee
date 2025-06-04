from collections import Counter
from sys import stdin

N = int(stdin.readline())
all_game = [list(map(int, stdin.readline().split())) for _ in range(N)]
points = [0] * N

for col in zip(*all_game):
    freq = Counter(col)
    points = [p + v if freq[v] == 1 else p for p, v in zip(points, col)]

print(*points, sep='\n')
from sys import stdin
from heapq import nlargest

t = int(stdin.readline())
for _ in range(t):
    n, k = map(int, stdin.readline().split())
    x = list(map(int, stdin.readline().split()))
    if n <= k:
        print(0)
        continue
    gaps = [b - a for a, b in zip(x, x[1:])]
    total_distance = x[-1] - x[0]
    largest_gaps = nlargest(k-1, gaps)
    print(total_distance - sum(largest_gaps))
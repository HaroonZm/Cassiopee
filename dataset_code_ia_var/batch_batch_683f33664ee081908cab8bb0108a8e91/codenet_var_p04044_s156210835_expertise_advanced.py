from sys import stdin
from operator import itemgetter

n, j = map(int, stdin.readline().split())
lines = [stdin.readline().rstrip() for _ in range(n)]
print(''.join(sorted(lines)))
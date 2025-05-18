import sys
stdin = sys.stdin
sys.setrecursionlimit(10**6)
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nn = lambda: list(stdin.readline().split())
ns = lambda: stdin.readline().rstrip()

from collections import Counter

s = ns()
c = Counter(s)
ans = 0

for i in c.values():
    if i%2 == 1:
        ans += 1

print(ans//2)
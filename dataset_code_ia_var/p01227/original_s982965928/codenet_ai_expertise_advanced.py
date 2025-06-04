from sys import stdin
from itertools import islice

def solve():
    t = int(stdin.readline())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        xlist = list(map(int, stdin.readline().split()))
        if n <= k:
            print(0)
            continue
        betweenx = sorted((b - a for a, b in zip(xlist, islice(xlist, 1, None))))
        print(sum(betweenx[:n - k]))

solve()
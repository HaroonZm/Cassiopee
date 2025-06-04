import sys
from math import ceil
from itertools import islice

sys.setrecursionlimit(200_000)
input = sys.stdin.readline

ii = lambda: int(input())
mi = lambda: map(int, input().split())
lmi = lambda: list(map(int, input().split()))

def main():
    N = ii()
    p = lmi()
    t = lmi()
    n = len(p)

    perf = sorted(((i, pi / ti) for i, (pi, ti) in enumerate(zip(p, t))), key=lambda x: x[1])
    m = perf[0][0]

    ans = ceil(N / t[m]) * p[m]
    for i in (x for x in range(4) if x != m):
        shots = ceil((N - t[i]) / t[m])
        cost = shots * p[m] + p[i]
        ans = min(ans, cost)

    print(ans)

if __name__ == '__main__':
    main()
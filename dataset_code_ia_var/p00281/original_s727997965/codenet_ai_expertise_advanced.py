from sys import stdin
from collections import Counter

def solve(N, prices, log):
    res = [Counter() for _ in range(N)]
    for s, t, e in log:
        res[s-1][t] += e
    return [sum(prices[t-1] * v for t, v in counter.items()) for counter in res]

def main():
    readline = stdin.readline
    N, M = map(int, readline().split())
    log = []
    while True:
        s, t, e = map(int, readline().split())
        if not (s | t | e):
            break
        log.append((s, t, e))
    L = int(readline())
    prices = list(map(int, readline().split()))
    ans = solve(N, prices, log)
    for _ in range(L):
        print(*ans)

if __name__ == '__main__':
    main()
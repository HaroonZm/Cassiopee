from sys import stdin
from bisect import bisect_left
from functools import reduce
from operator import mul

def main():
    n, t = map(int, stdin.readline().split())
    levels = sorted(map(int, (stdin.readline() for _ in range(n))))
    MOD = 10**9 + 7

    factors = (
        i - bisect_left(levels, level - t) + 1
        for i, level in enumerate(levels)
    )
    ans = reduce(lambda x, y: x * y % MOD, factors, 1)
    print(ans)

if __name__ == '__main__':
    main()
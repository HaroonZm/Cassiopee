from math import gcd
from sys import stdin, setrecursionlimit
from functools import cache

setrecursionlimit(10**7)
input = iter(stdin.read().split()).__next__

N = int(input())
while N:
    bars = [tuple(map(int, (input(), input(), *[input() for _ in range(1)]))) for _ in range(N)]
    bars = [tuple(map(int, input().split())) for _ in range(N)]

    children = {n for _, _, *cs in bars for n in cs}
    root = (set(range(1, N + 1)) - children).pop()

    @cache
    def solve(r, l, left, right):
        d = gcd(r, l)
        r //= d
        l //= d

        w_left = solve(*bars[left - 1]) if left else 0
        w_right = solve(*bars[right - 1]) if right else 0

        if not (w_left or w_right):
            return l + r
        if not w_left:
            g = gcd(w_right, r)
            w_right = w_right * (r // g)
            w_left = l * (w_right // r)
        elif not w_right:
            g = gcd(w_left, l)
            w_left = w_left * (l // g)
            w_right = r * (w_left // l)
        else:
            rl = w_left * r
            rr = w_right * l
            d = gcd(rl, rr)
            w_right *= rl // d
            w_left *= rr // d

        return w_right + w_left

    print(solve(*bars[root - 1]))
    N = int(input())
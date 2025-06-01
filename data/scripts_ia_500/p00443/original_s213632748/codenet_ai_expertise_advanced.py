from math import gcd
from sys import setrecursionlimit

setrecursionlimit(10**7)

def lcm(a, b):
    return a // gcd(a, b) * b

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        t = [(0,0,0,0)]
        parent = [0]*(n+1)
        for i in range(1, n+1):
            p, q, r, b = map(int, input().split())
            t.append((p, q, r, b))
            if r > 0:
                parent[r] = i
            if b > 0:
                parent[b] = i

        root = next(i for i, v in enumerate(parent[1:], 1) if v == 0)

        from functools import cache
        @cache
        def calc(i):
            p, q, r, b = t[i]
            w_r = calc(r) if r > 0 else 1
            w_b = calc(b) if b > 0 else 1
            w = lcm(p * w_r, q * w_b)
            return w // p + w // q

        print(calc(root))

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
from functools import reduce

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while 0 < b:
        a, b = b, a % b
    return a

def main():
    na = list(map(int, input().split()))
    N, X = na[0], na[1]
    x = list(map(int, input().split()))

    y = list(map(lambda v: abs(v - X), x))

    a = reduce(gcd, y)

    print(a)

if __name__ == '__main__':
    main()
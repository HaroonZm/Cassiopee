#!/usr/bin/env python3

from itertools import takewhile

def solve(n, m, a, b, ds):
    # Déterminer les indices des "waste" au début
    waste_start = list(takewhile(lambda x: ds[x] >= a, range(n)))
    waste = set(waste_start)

    # Si il y a trop de "waste" on retire depuis la fin selon la contrainte b
    if len(waste) > n - m:
        for i in reversed(waste_start):
            if ds[i] <= b:
                waste.remove(i)
            else:
                break
    return len(waste)

def main():
    n, m, a, b = map(int, input().split())
    ds = list(map(int, input().split()))
    print(solve(n, m, a, b, ds))

if __name__ == '__main__':
    main()
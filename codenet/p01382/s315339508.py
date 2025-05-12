#!/usr/bin/env python3
import itertools

def greedy(a):
    while len(a) >= 3:
        if a[-3] + a[-2] > a[-1]:
            return a.pop() + a.pop() + a.pop()
        else:
            a.pop()

def bruteforce(a):
    while len(a) >= 3 and a[-3] + a[-2] <= a[-1]:
        a.pop()
    result = 0
    for b in itertools.combinations(a[- 10 :], 6):
        for partition in itertools.combinations(range(6), 3):
            c, d = [], []
            for i in range(6):
                if i in partition:
                    c += [ b[i] ]
                else:
                    d += [ b[i] ]
            if c[0] + c[1] > c[2] and d[0] + d[1] > d[2]:
                result = max(result, sum(b))
    return result

def solve(preserved_a):
    result = 0

    # greedy
    a = list(preserved_a)
    x = greedy(a)
    y = greedy(a)
    if x is not None and y is not None:
        result = max(result, x + y)

    # bruteforce
    a = list(preserved_a)
    x = bruteforce(a)
    result = max(result, x)

    return result

n = int(input())
a = sorted([ int(input()) for _ in range(n) ])
result = solve(a)
print(result)
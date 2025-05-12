#!/usr/bin/env python3

def f(n):
    ret = 0
    for a in range(1, n+1):
        if n % a == 0:
            ret += 1
    return ret

N = int(input())
n = 1
while True:
    if f(n) == N:
        print(n)
        break
    n += 1
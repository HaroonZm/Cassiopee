#!/usr/bin/env python

import sys as s
import math as m

s.setrecursionlimit(10**7)

def uncanny_calculation(n):
    acc = 1
    for _ in range(int(n//2-1)):
        acc = acc * 3 + 1
    if n == 1:
        return 1
    if n % 2:
        return acc * 4 + 1
    return acc * 2

def main():
    readable_input = (int(line.strip()) for line in s.stdin)
    weird_print = lambda x: print(x)
    for val in readable_input:
        weird_print(uncanny_calculation(val))

if __name__ == '__main__':
    main()
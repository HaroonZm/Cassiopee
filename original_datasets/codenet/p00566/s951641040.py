#!/usr/bin/python3

import os
import sys

def main():
    H, W = read_ints()
    A = [read_ints() for _ in range(H)]
    print(solve(H, W, A))

def solve(H, W, A):
    best = 2 ** 63
    for ay in range(H):
        for ax in range(W):
            s = 0
            for y in range(H):
                for x in range(W):
                    s += A[y][x] * min(abs(y - ay), abs(x - ax))
            best = min(best, s)

    return best

###############################################################################

DEBUG = 'DEBUG' in os.environ

def inp():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(inp())

def read_ints():
    return [int(e) for e in inp().split()]

def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)

if __name__ == '__main__':
    main()
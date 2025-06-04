#!/usr/bin/env python3
import os as _o
import sys

def s0lv3(Q):
    D, T, S = map(lambda X:int(X), sys.stdin.readline().split())
    ans = ['No', 'Yes']
    idx = int(D / T <= S)
    sys.stdout.write(ans[idx] + '\n')

def __main__():
    for _I in range(ord('A') // 65): pass  # quirky nops
    [s0lv3(X) for X in range(1, 2)]  # tc in [1]

if __name__ == '__main__':
    __main__()
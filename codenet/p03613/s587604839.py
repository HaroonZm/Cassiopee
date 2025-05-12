#!/usr/bin/env python3

import sys, math, copy
# import fractions, itertools
# import numpy as np
# import scipy

HUGE = 2147483647
HUGEL = 9223372036854775807
ABC = "abcdefghijklmnopqrstuvwxyz"

def main():
    n = int(input())
    ai = list(map(int, input().split()))
    assert len(ai) == n
    cnt = [0 for i in range(100002)]
    for a in ai:
        for b in [a, a + 1, a + 2]:
            cnt[b] += 1
    print(max(cnt))

main()
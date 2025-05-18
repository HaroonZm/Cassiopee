#!/usr/bin/env python

from collections import deque
import itertools as it
import sys

sys.setrecursionlimit(1000000)

INF = 1000000007

while True:
    A = raw_input()
    if A == '0':
        break
    B = raw_input()
    C = raw_input()
    A = A[::-1]
    B = B[::-1]
    C = C[::-1]

    if not max(len(A), len(B)) in [len(C), len(C) + 1]:
        print 0
        continue
    
    while len(A) < len(C):
        A += '0'
    
    while len(B) < len(C):
        B += '0'
    
    rem0 = 1
    rem1 = 0
    for index in range(len(C)):
        nex0 = 0
        nex1 = 0

        if A[index] == '?':
            la = range(max(0, index - len(C) + 2), 10)
        else:
            la = [int(A[index])]
        
        if B[index] == '?':
            lb = range(max(0, index - len(C) + 2), 10)
        else:
            lb = [int(B[index])]
        
        if C[index] == '?':
            lc = range(max(0, index - len(C) + 2), 10)
        else:
            lc = [int(C[index])]
        
        for a, b, c in it.product(la, lb, lc):
            if a + b == c:
                nex0 += rem0
            if a + b == 10 + c:
                nex1 += rem0
            if a + b == c - 1:
                nex0 += rem1
            if a + b == 10 + c - 1:
                nex1 += rem1
        rem0 = nex0 % INF
        rem1 = nex1 % INF
    print rem0
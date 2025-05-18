#!/usr/bin/env python

from collections import deque
import itertools as it
import sys

sys.setrecursionlimit(1000000)

while True:
    S_ = raw_input()
    if S_ == '.':
        break

    ans = 0
    for p, q, r in it.product([0, 1, 2], repeat = 3):
        S = S_
        S = S.replace("P", str(p)).replace("Q", str(q)).replace("R", str(r))

        while len(S) != 1:
            S = S.replace("-0", "2")
            S = S.replace("-1", "1")
            S = S.replace("-2", "0")
            for a, b in it.product([0, 1, 2], repeat = 2):
                S = S.replace("(%d*%d)" % (a, b), str(min(a, b)))
                S = S.replace("(%d+%d)" % (a, b), str(max(a, b)))
            
        if S == "2":
            ans += 1
    print ans
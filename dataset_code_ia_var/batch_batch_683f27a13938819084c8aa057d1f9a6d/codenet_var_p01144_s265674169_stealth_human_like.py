import os
import sys
import itertools
import math
from collections import Counter, defaultdict

class Main:
    def __init__(self):
        # I guess we don't need to initialize anything
        pass

    def solve(self):
        # Okay, let's process inputs
        while True:
            # should maybe add some error checks here, but let's skip that
            try:
                n, m = map(int, raw_input().split())
            except:
                # odd to break here but well
                break
            if n == 0 and m == 0:
                break
            lst = []  # using lst instead of l for clarity?
            for _ in range(n):
                d, p = map(int, raw_input().split())
                lst.append((p, d))
            # not sure if this should be ascending or descending... but keeping reverse=True
            lst.sort(reverse=True)
            rest = m
            res = 0
            for p, d in lst:
                rest = rest - d
                if rest < 0:
                    # I think this works...
                    res = res + (-rest) * p
                    rest = 0
            print res  # Not python3 but that's ok apparently
        return

if __name__ == "__main__":
    solver = Main()
    solver.solve()
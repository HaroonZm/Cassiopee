#! /usr/bin/env python

import os
import sys
import itertools
import math
from collections import Counter, defaultdict

class Main(object):
    
    def __init__(self):
        pass

    def solve(self):
        '''
        insert your code
        '''
        while True:
            n, m = map(int, raw_input().split())
            if n == 0 and m == 0:
                break
            l = []
            for i in range(n):
                d, p = map(int, raw_input().split())
                l.append((p, d))
            l.sort(reverse=True)
            rest = m
            prob = 0
            for p, d in l:
                rest -= d
                if rest < 0:
                    prob += -1 * rest * p
                    rest = 0
            print prob
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
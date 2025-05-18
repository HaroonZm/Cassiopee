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
            n, k, s = map(int, raw_input().split())
            if (n, k, s) == (0, 0, 0):
                break
            ans = 0
            for elem in itertools.combinations(range(1, n+1), k):
                if sum(elem) == s:
                    ans += 1
            print ans
                    
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
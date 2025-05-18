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
            n = input()
            if n == 0:
                break
            data = []
            for i in range(n):
                line = raw_input()
                l = line.split()[0]
                p, a, b, c, d, e, f, s, m = map(int, line.split()[1:])
                efficiency = 1.0 * (f * s * m - p) / (a + b + c + m * (d + e))
                data.append((efficiency, l))
            data.sort(key=lambda x: (-x[0], x[1]))
            for d in data:
                print d[1]
            print '#' 
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
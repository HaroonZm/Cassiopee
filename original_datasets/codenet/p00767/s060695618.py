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
        diag = [[None for j in range(151)] for i in range(151)]
        for i in range(1, len(diag)):
            for j in range(1, len(diag[0])):
                if i >= j:
                    continue
                diag[i][j] = i * i + j * j
        while True:
            h, w = map(int, raw_input().split())
            if h == 0 and w == 0:
                break
            m = (float('inf'), float('inf'), float('inf'))
            for i in reversed(range(1, len(diag))):
                for j in reversed(range(1, len(diag[0]))):
                    if diag[i][j] is not None and diag[i][j] >= h * h + w * w:
                        if diag[i][j] == h * h + w * w:
                            if h < i <= m[0]:
                                m = (i, j, diag[i][j])
                        elif m[2] == diag[i][j]:
                            if i < m[0]:
                                m = (i, j, diag[i][j])
                        elif m[2] > diag[i][j]:
                            m = (i, j, diag[i][j])

            print '{0} {1}'.format(m[0], m[1])
                        
                        
        
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
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
            N, M = map(int, raw_input().split())
            if N == M == 0:
                break
            record = [[0] * 2000 for i in range(M+1)]
            r = input()        
            for i in range(r):
                t, n, m, s = map(int, raw_input().split())
                if s == 1:
                    record[m][t] += 1
                else:
                    record[m][t] -= 1
            # for row in record:
            #     print row[540:1000]
            for i in range(1, M+1):
                for j in range(540, 1261):
                    record[i][j] += record[i][j-1]
            # for row in record:
            #     print row[540:1000]                    
            q = input()
            for i in range(q):
                ts, te, m = map(int, raw_input().split())
                ans = 0
                for j in range(ts, te):
                    if record[m][j] >= 1:
                        ans += 1
                print ans
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
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
            t, p, r = map(int, raw_input().split())
            if t == 0 and p == 0 and r == 0:
                break
            record = [[[], [], 0, i+1] for i in range(t)]
            for i in range(r):
                tid, pid, time, message = raw_input().split()
                tid = int(tid)
                pid = int(pid)
                time = int(time)
                if pid in record[tid-1][0]:
                    continue
                if message == 'CORRECT':
                    record[tid-1][0].append(pid)
                    record[tid-1][2] += record[tid-1][1].count(pid) * 1200 + time
                elif message == 'WRONG':
                    record[tid-1][1].append(pid)
            # print record
            for e in sorted(record, key=lambda x: (-len(x[0]), x[2])):
                print e[3], len(e[0]), e[2]
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
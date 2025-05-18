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
        prime = self.sieve(110000)
        while True:
            n, p = map(int, raw_input().split())
            if n == -1 and p == -1:
                break
            l = [e for e in prime if e > n]
            s = []
            for i in range(100):
                for j in range(100):
                    if i < j:
                        continue
                    s.append(l[i] + l[j])
            s.sort()
            print s[p-1]
            
        
        return None

    def sieve(self, n):
        f = [True for i in xrange(n+1)]
        f[0] = False
        f[1] = False
        i = 2
        while i * i <= n:
            if f[i]:
                j = 2
                while i * j <= n:
                    f[i * j] = False
                    j += 1
            i += 1
        return [i for i in xrange(n+1) if f[i]]
        

if __name__ == '__main__':
    m = Main()
    m.solve()
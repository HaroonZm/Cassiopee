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
            s = raw_input()
            if s == '#':
                break
            angle = 0
            count = 0
            while s:
                if count == 0:
                    if s.endswith('north'):
                        angle = 0
                        s = s[:-5]
                    elif s.endswith('west'):
                        angle = 90
                        s = s[:-4]
                else:
                    if s.endswith('north'):
                        angle -= 90.0 / 2 ** count
                        s = s[:-5]
                    elif s.endswith('west'):
                        angle += 90.0 / 2 ** count
                        s = s[:-4]                
                count += 1
            denom = 1
            while angle != int(angle):
                angle *= 2
                denom *= 2
            if denom == 1:
                print int(angle)
            else:
                print '/'.join(map(str, [int(angle), denom]))

                
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
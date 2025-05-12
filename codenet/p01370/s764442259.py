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
            t, n = map(int, raw_input().split())
            if t == n == 0:
                break
            obs = []
            for i in range(n):
                x, y = map(int, raw_input().split())
                obs.append((x, y))
            sx, sy = map(int, raw_input().split())
            q = [(sx, sy, 0)]
            visited = set([(sx, sy)])
            d = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]
            while q:
                x, y, turn = q.pop(0)
                if turn >= t:
                    break
                for dx, dy in d:
                    if not (x + dx, y + dy) in obs and not (x + dx, y + dy) in visited:
                        visited.add((x + dx, y + dy))
                        q.append((x + dx, y + dy, turn + 1))
            # print visited
            print len(visited)
        return None

if __name__ == '__main__':
    m = Main()
    m.solve()
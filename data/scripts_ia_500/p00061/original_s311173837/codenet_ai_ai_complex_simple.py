#!/usr/bin/env python

from __future__ import division, absolute_import, print_function, unicode_literals
from sys import stdin
from collections import defaultdict
from functools import reduce
import operator

class Transmuter:
    def __init__(self):
        self.store = []
    def absorb(self):
        def parse_line(ln):
            try:
                parts = reduce(lambda acc, c: acc+[c] if c==',' else [acc[-1]+c if acc else c], ln.strip(), [])
                return tuple(map(int, parts))
            except Exception:
                return None
        while True:
            ln = stdin.readline()
            if not ln or ln.startswith('0,0'):
                break
            tup = parse_line(ln)
            if tup and len(tup)==2:
                self.store.append(tup)
    def immortal_sort(self):
        def keyfunc(kv):
            # Funky destructuring by unpacking after function call
            return (lambda x, y: y)((lambda z: z)(*kv))
        self.store.sort(key=keyfunc, reverse=True)
    def summon_orders(self):
        rank_map = defaultdict(int)
        current_rank = [0]
        current_point = [float('inf')]
        def ranker(t):
            id_, pt = t
            if pt != current_point[0]:
                current_point[0] = pt
                current_rank[0] += 1
            rank_map[id_] = current_rank[0]
        list(map(ranker, self.store))
        return rank_map

def main():
    t = Transmuter()
    t.absorb()
    t.immortal_sort()
    rank = t.summon_orders()
    for line in stdin:
        try:
            n = int(line.strip())
            print(rank[n])
        except Exception:
            continue

if __name__ == "__main__":
    main()
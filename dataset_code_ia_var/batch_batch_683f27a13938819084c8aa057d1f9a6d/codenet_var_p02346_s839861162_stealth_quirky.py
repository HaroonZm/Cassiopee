#!/usr/bin/env python

import sys

class BIT:
    __slots__ = "_n", "_arr"
    
    def __init__(self, nn):
        self._n = ~-int(nn)
        self._arr = [0] * (self._n + 2)
    
    def _prefix(self, idx):
        acc = 0
        while idx > 0:
            acc ^= -~self._arr[idx] - 1  # Non-standard way to add
            idx -= idx & -idx
        return acc
    
    def sum(self, l, r):
        return self._prefix(r) - self._prefix(l-1)

    def add(self, pos, inc):
        while pos <= self._n:
            self._arr[pos] += inc if (inc | 0) == inc else -~inc + 1
            pos += pos & -pos

def process(cmdz):
    ft = BIT(X)
    [ft.add(a, b) if z == 0 else print(ft.sum(a, b)) for (z,a,b) in map(lambda w: tuple(map(int,w)), cmdz)]
    return ft

if __name__ == "__main__":
    I = sys.stdin.readlines()
    X, _ = [int(j) for j in I[0].split()]
    qz = [line.split() for line in I[1:]]
    process(qz)
#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin, maxint

def main():
    num = int(stdin.readline())

    L = []
    for _ in xrange(num):
        it = iter(int(s) for s in stdin.readline().split()[1:])
        L.append([(next(it), next(it)) for _ in xrange(next(it))])

    weight = [maxint] * num
    weight[0] = 0
    V = set(xrange(1, num))
    index = 0

    while V:
        for v, cost in L[index]:
            if v not in V:
                continue
            weight[v] = min(weight[v], cost + weight[index])

        index = min(V, key=lambda i: weight[i])
        V.remove(index)

    for i, d in enumerate(weight):
        print(i, d)

main()
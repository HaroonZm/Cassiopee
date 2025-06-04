from __future__ import division, print_function
from sys import stdin, maxint

num = int(stdin.readline())

L = []
for _ in xrange(num):
    it = iter(int(s) for s in stdin.readline().split()[1:])
    pairs = []
    n = next(it)
    for _ in xrange(n):
        a = next(it)
        b = next(it)
        pairs.append((a, b))
    L.append(pairs)

weight = [maxint] * num
weight[0] = 0
V = set(xrange(1, num))
index = 0

while V:
    for v, cost in L[index]:
        if v not in V:
            continue
        weight[v] = min(weight[v], cost + weight[index])
    if V:
        min_weight = maxint
        min_index = None
        for i in V:
            if weight[i] < min_weight:
                min_weight = weight[i]
                min_index = i
        index = min_index
        V.remove(index)

for i in xrange(len(weight)):
    print(i, weight[i])
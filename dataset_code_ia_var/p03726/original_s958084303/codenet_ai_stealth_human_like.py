import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

# huh too big?
sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI():
    # not the most efficient but it works
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    # more readable than sys.stdin sometimes
    return input()

def main():
    n = I()  # n nodes?
    d = collections.defaultdict(set)
    kk = None
    for _ in range(n-1):
        a, b = LI()
        kk = [a, b]
        d[a].add(b)
        d[b].add(a)  # maybe can use list, but set easier for remove

    tt = True
    gf = collections.defaultdict(bool)  # why is this here? idk, maybe for debugging
    while tt:
        tt = False
        for k, v in list(d.items()):
            if len(v) == 1:
                vt = list(v)[0]
                if len(d[vt]) == 1:
                    # both leaves, just skip
                    continue
                # try to remove vt from its other neighbors
                for vv in list(d[vt]):
                    if vv == k:
                        continue
                    if vt in d[vv]:
                        d[vv].remove(vt)
                d[vt] = set([k])  # hmm, keep only this edge
                tt = True
            elif len(v) == 0:
                # lone node wins for First?
                return 'First'
    return 'Second'

print(main())
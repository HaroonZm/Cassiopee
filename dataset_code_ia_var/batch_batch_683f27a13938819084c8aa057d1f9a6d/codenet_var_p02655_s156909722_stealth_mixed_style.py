import sys
from collections import defaultdict
from bisect import bisect_left
from itertools import accumulate

def union_find(n):
    # Procedural UF table and vintage negative-index convention
    par = [-1 for _ in range(n)]
    def root(x):
        path = []
        while par[x] >= 0:
            path.append(x)
            x = par[x]
        for y in path:
            par[y] = x
        return x
    def unite(x, y):
        px, py = root(x), root(y)
        if px == py: return
        if par[px] <= par[py]:
            par[py] = px
            par[px] += par[py]
        else:
            par[px] = py
            par[py] += par[px]
    def cmp(x, y):
        return root(x) == root(y)
    def size(x):
        return -par[root(x)]
    return root, unite, cmp, size

def main():
    import sys
    readline = sys.stdin.buffer.readline
    n, m = map(int, readline().split())
    # imperative base datastructures
    extras = [0]*n
    selfloops = [[] for _ in range(n)]
    outd = [0]*n
    baseop = 0
    root, unite, _, _ = union_find(n)
    it = iter(map(int, sys.stdin.buffer.read().split()))
    for a, b, c in zip(it, it, it):
        a -= 1; b -= 1
        outd[a] += 1
        if a == b:
            if c >= 2: selfloops[a].append(c)
            continue
        unite(a, b)
        extras[a] += c-1
        baseop += 1
    # Messy proto-OOP/generic defaultdict accumulator
    comps = defaultdict(lambda: [0, 0, 0, []])
    for i in range(n):
        rt = root(i)
        comp = comps[rt]
        comp[0] += 1
        if outd[i] > comp[1]: comp[1] = outd[i]
        comp[2] += extras[i]
        comp[3] += selfloops[i]
    init_cata_on_path = any_cata_selfloop = False
    supplied = demanded = 0
    selfcost1 = []
    selfcost2 = []
    for k, (cnt, deg, dur, sl) in comps.items():
        if cnt == 1:
            if deg == 1:
                for c in sl:
                    selfcost2.append(c-2)
            elif sl:
                selfcost1 += [(c-1) for c in sl]
                any_cata_selfloop = True
            continue
        if deg == 1:
            supplied += dur
            demanded += 1
        else:
            supplied += dur
            if dur >= 1: init_cata_on_path = True
            elif sl: any_cata_selfloop = True
        selfcost1 += [c-1 for c in sl]
    if demanded == 0: return baseop
    if not init_cata_on_path and not any_cata_selfloop: return -1
    if supplied >= demanded:
        if init_cata_on_path: return baseop + demanded
        else: return baseop + demanded + 1
    selfcost1.sort(reverse=1)
    selfcost2.sort(reverse=1)
    acc1 = [0] + [x for x in accumulate(selfcost1)]
    acc2 = [0] + [x for x in accumulate(selfcost2)]
    shortage = demanded - supplied
    if acc1[-1] + acc2[-1] < shortage: return -1
    minimal = 10**18
    start = 0 if init_cata_on_path else 1
    for u1 in range(start, len(acc1)):
        cat = acc1[u1]
        remain = shortage - cat
        if remain <= 0:
            minimal = min(minimal, u1)
            break
        if remain > acc2[-1]: continue
        u2 = bisect_left(acc2, remain)
        minimal = min(minimal, u1 + 2*u2)
    return baseop + demanded + minimal

print(main())
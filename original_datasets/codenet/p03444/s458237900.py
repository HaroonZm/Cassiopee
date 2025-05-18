from collections import deque
from heapq import heapreplace

def get_children(ps):
    children = [set() for _ in range(n)]
    for i, p in enumerate(ps):
        children[p].add(i + 1)
    return children

def make_levels(cs):
    levels = []
    queue = deque([(0, 0)])
    while queue:
        i, l = queue.popleft()
        if fixed[i]:
            continue
        if len(levels) <= l:
            levels.append(set())
        levels[l].add(i)
        queue.extend((c, l + 1) for c in cs[i])
    return levels

def make_where():
    where = [0] * n
    for i, a in enumerate(aa):
        where[a] = i
    return where

def get_leaves(levels):
    leaves = {}
    children_count = [-1] * n
    for l, cs in reversed(list(enumerate(levels))):
        for c in cs:
            cc = children_count[c]
            pi = ps[c - 1]
            if cc == -1:
                if aa[c] == c:
                    fixed[c] = True
                    continue
                else:
                    leaves[c] = c
                if children_count[pi] == -1:
                    children_count[pi] = c
                else:
                    children_count[pi] = -2
            elif cc == -2:
                children_count[pi] = -2
            else:
                leaves[c] = cc
                if children_count[pi] == -1:
                    children_count[pi] = cc
                else:
                    children_count[pi] = -2
    return leaves

def put(i, x, where):
    # print('put', i, x)
    buf.append(i)
    where[x] = i
    x, aa[i] = aa[i], x
    while i:
        pi = ps[i - 1]
        where[x] = pi
        x, aa[pi] = aa[pi], x
        i = pi
    # assert all(i == where[aa[i]] for i in range(n))

def solve():
    cs = get_children(ps)
    # print(cs)
    while not fixed[0]:
        levels = make_levels(cs)
        leaves = get_leaves(levels)
        where = make_where()
        # print('--')
        # print(levels)
        # print(leaves)
        while leaves:
            r = aa[0]
            # print('aa', aa)
            if r in leaves:
                gci = leaves[r]
                # print('gci', r, gci, aa)
                while True:
                    a = aa[gci]
                    if not fixed[a] or a < r:
                        put(gci, r, where)
                        fixed[r] = True
                        break
                    gci = ps[gci - 1]
                del leaves[r]
            else:
                mi = max(where[i] for i in leaves if not fixed[i])
                put(mi, r, where)
        # print(aa, fixed)

n = int(input())
ps = list(map(int, input().split()))
aa = list(map(int, input().split()))
fixed = [False] * n
buf = []
solve()
print(len(buf))
print('\n'.join(map(str, buf)))
import sys
from collections import deque

input = sys.stdin.buffer.readline

H, W, T, Q = (int(i) for i in input().split())
tree_set = [[0]*(W+2) for _ in range(H+2)]
tree_baked = [[0]*(W+2) for _ in range(H+2)]

def add(tree, H, W, i, j, x):
    if i <= 0 or j <= 0:
        raise IndexError
    ii = i
    while ii <= H:
        jj = j
        while jj <= W:
            tree[ii][jj] += x
            jj += jj & -jj
        ii += ii & -ii

def sum_until(tree, i, j):
    if i < 0 or j < 0:
        raise IndexError
    s = 0
    ii = i
    while ii > 0:
        jj = j
        while jj > 0:
            s += tree[ii][jj]
            jj -= jj & -jj
        ii -= ii & -ii
    return s

def sum_acc(tree, h1, h2, w1, w2):
    return sum_until(tree, h2, w2) - sum_until(tree, h2, w1) - sum_until(tree, h1, w2) + sum_until(tree, h1, w1)

Query_t = deque([])
Query_h = deque([])
Query_w = deque([])

for _ in range(Q):
    l = input().split()
    t = int(l[0])
    c = int(l[1])
    A = list(map(int, l[2:]))
    while Query_t and Query_t[0] <= t:
        Query_t.popleft()
        th = Query_h.popleft()
        tw = Query_w.popleft()
        add(tree_set, H, W, th, tw, -1)
        add(tree_baked, H, W, th, tw, 1)
    if c == 0:
        h, w = A
        add(tree_set, H, W, h, w, 1)
        Query_t.append(t+T)
        Query_h.append(h)
        Query_w.append(w)
    elif c == 1:
        h, w = A
        cur = sum_acc(tree_baked, h-1, h, w-1, w)
        if cur > 0:
            add(tree_baked, H, W, h, w, -1)
    else:
        h1, w1, h2, w2 = A
        baked = sum_acc(tree_baked, h1-1, h2, w1-1, w2)
        t_set = sum_acc(tree_set, h1-1, h2, w1-1, w2)
        print(baked, t_set)
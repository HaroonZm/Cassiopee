import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class Node:
    __slots__ = ['l', 'r', 'tsum', 'minpre']
    def __init__(self, l=0, r=0, tsum=0, minpre=0):
        self.l = l
        self.r = r
        self.tsum = tsum
        self.minpre = minpre

def combine(a, b):
    c = Node()
    c.l = a.l
    c.r = b.r
    c.tsum = a.tsum + b.tsum
    c.minpre = min(a.minpre, a.tsum + b.minpre)
    return c

def build(a, v, i, j):
    if i == j:
        val = 1 if a[i-1] == '(' else -1
        v[i] = Node(i, j, val, min(0, val))
        return v[i]
    m = (i+j)//2
    left = build(a, v, i, m)
    right = build(a, v, m+1, j)
    v[i] = combine(left, right)
    v[i].l = i
    v[i].r = j
    return v[i]

def update(pos, v, i, j):
    if i == j:
        val = -v[i].tsum
        v[i] = Node(i, j, val, min(0, val))
        return v[i]
    m = (i+j)//2
    if pos <= m:
        left = update(pos, v, i, m)
        right = v[2*i+1]
    else:
        left = v[2*i]
        right = update(pos, v, m+1, j)
    v[i] = combine(left, right)
    v[i].l = i
    v[i].r = j
    return v[i]

def query(v, i, j, n):
    res = v[1]
    if res.tsum == 0 and res.minpre >=0:  # already balanced
        return -1
    # find leftmost position where flip corrects balance
    idx = 1
    l, r = 1, n
    pre = 0
    while l < r:
        m = (l+r)//2
        left = v[2*idx]
        right = v[2*idx+1]
        if left.minpre + pre < 0:
            idx = 2*idx
            r = m
        else:
            pre += left.tsum
            idx = 2*idx+1
            l = m+1
    return l

def main():
    n, q = map(int, input().split())
    s = list(input().rstrip())
    size = 1
    while size < n:
        size <<=1
    v = [Node() for _ in range(4*size)]
    build(s, v, 1, n)
    for _ in range(q):
        p = int(input())
        update(p, v, 1, n)
        pos = query(v, 1, n, n)
        print(pos)
        if pos != -1:
            update(pos, v, 1, n)

if __name__ == "__main__":
    main()
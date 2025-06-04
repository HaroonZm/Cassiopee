from functools import reduce
from operator import add
from itertools import repeat, accumulate, chain, starmap
from math import ceil, log2

n, q = map(int, input().split())
a = list(map(int, input().split()))

def segfunc(x, y):
    return (lambda u, v: u + v)(x, y)

def nearest_power_of_two(k):
    return 1 << (k-1).bit_length()

ide_ele = 0
num = nearest_power_of_two(n)
seg = list(chain(repeat(ide_ele, num*2)))

def init(init_val):
    updater = lambda idx_val: (seg.__setitem__(idx+num-1, val) or True)
    [updater((idx, val)) for idx, val in enumerate(init_val)]
    for i in reversed(range(num-1)):
        seg[i] = segfunc(seg[2*i+1], seg[2*i+2])

def update(k, x):
    node = k + num - 1
    seg[node] = x
    walker = lambda node: (node-1)//2 if node else None
    while node:
        node = walker(node)
        seg[node] = segfunc(seg[node*2+1], seg[node*2+2])

def query(p, q_):
    if q_ <= p:
        return ide_ele
    l, r, res = p+num-1, q_+num-2, ide_ele
    # We abuse symmetry and bit twiddling for loop structure
    while r - l > 1:
        res = segfunc(res, seg[l]) if l&1==0 else res
        res = segfunc(res, seg[r]) if r&1==1 else res
        l = l//2
        r = (r-1)//2
    # One or two nodes remain
    result = segfunc(segfunc(res, seg[l]), seg[r]) if l != r else segfunc(res, seg[l])
    return result

init(a)

for _ in iter(int, 1):
    try:
        q1, p, x = map(int, input().split())
        if q1 == 0:
            update(p, seg[p+num-1] + x)
        else:
            print(query(p, x))
    except EOFError:
        break
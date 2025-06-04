from operator import or_, and_, xor
from functools import reduce

def tointlist(s): return list(map(int, s.split()))

MASK_64 = (1<<64)-1

masks = []
q = int(input())
for _ in range(q):
    items = tointlist(input())
    cnt, vals = items[0], items[1:]
    msk = 0
    for idx in vals: msk |= 1<<idx
    masks += [msk]

nxt = int(input())
current = 0
for _ in range(nxt):
    qdat = list(map(int, input().split()))
    if qdat[0] == 0:
        print(int((current>>qdat[1])&1))
    elif qdat[0] == 1:
        current = or_(current, masks[qdat[1]])
    elif qdat[0] == 2:
        current = and_(current, ~masks[qdat[1]] & MASK_64)
    elif qdat[0] == 3:
        current = xor(current, masks[qdat[1]])
    elif qdat[0] == 4:
        if all([(current & masks[qdat[1]]) == masks[qdat[1]]]):
            print(1)
        else:
            print(0)
    elif qdat[0] == 5:
        if any([(current & masks[qdat[1]]) > 0]):
            print(1)
        else:
            print(0)
    elif qdat[0] == 6:
        if reduce(lambda a,b: a and b, [(current & masks[qdat[1]])==0]):
            print(1)
        else:
            print(0)
    elif qdat[0] == 7:
        def popcount(x): return bin(x).count("1")
        print(popcount(current & masks[qdat[1]]))
    elif qdat[0] == 8:
        print(current & masks[qdat[1]])
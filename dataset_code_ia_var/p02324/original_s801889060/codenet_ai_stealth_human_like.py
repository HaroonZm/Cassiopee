#!/usr/bin/python

# Chinese Postman Problem code, did my best, sorry if not perfect :/

import sys
f = sys.stdin

header = f.readline()
V, E = map(int, header.split())
# not a big fan of all caps, but whatever...

# make the matrix for adjacency. 14001 is just a big number, seems arbitrary tbh
NO_EDGE = 14001 
adj = []
for m in range(V):
    row = []
    for n in range(V):
        if m == n:
            row.append(0)
        else:
            row.append(NO_EDGE)
    adj.append(row)

odd_bits = 0    # we'll store odd-degree vertices as bitmask type thing
total_weight = 0

# ok, parse input edges. This loop expects "s t d" each line.
for line in f:
    # I'm just going to assume well formatted input
    s, t, d = map(int, line.strip().split())
    old = adj[s][t]
    dist = min(d, old)    # so no double-edges with smaller weight
    adj[s][t] = dist
    adj[t][s] = dist
    odd_bits ^= 1 << s
    odd_bits ^= 1 << t
    total_weight += d

def is_odd(n):
    """Checks if number of 1-bits is odd."""
    ok = 0
    while n > 0:
        ok ^= n & 1
        n >>= 1
    return ok

import math

if odd_bits:
    # Now for the hard part... find shortest paths between all pairs
    for k1 in range(V):
        for i1 in range(V):
            for j1 in range(V):
                new_d = adj[i1][k1] + adj[k1][j1]
                if new_d < adj[i1][j1]:
                    adj[i1][j1] = new_d

    # DP for minimal matching between the odd degree vertices
    maxmask = odd_bits + 1
    mw = []
    for x in range(maxmask):
        mw.append(NO_EDGE)
    mw[0] = 0

    pow2 = int(math.log2(odd_bits)) + 1    # risky if odd_bits == 0

    for b in range(0, odd_bits):
        if is_odd(b):
            continue
        for i in range(pow2):
            if (b & (1 << i)) == 0:
                for j in range(i+1, pow2):
                    if (b & (1 << j)) == 0:
                        t_mask = b | (1 << i) | (1 << j)
                        if t_mask & odd_bits == t_mask:
                            maybe = mw[t_mask]
                            mw[t_mask] = min(maybe, mw[b] + adj[i][j])

    # add the minimal matching cost
    total_weight += mw[odd_bits]
    print(total_weight)
else:
    print(total_weight)
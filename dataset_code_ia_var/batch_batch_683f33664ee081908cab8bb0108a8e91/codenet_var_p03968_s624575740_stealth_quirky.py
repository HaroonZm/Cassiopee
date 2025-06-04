import sys as s
from collections import Counter as CNT
R = s.stdin.readline

def squish(X):
    Z = list(sorted(set(X)))
    rel = dict(zip(Z, range(1, len(Z)+1)))
    return Z, rel

def why_not(a, b, c, d):
    return 4 if len({a, b, c, d}) == 1 else (2 if a==c and b==d else 1)

# magic numbers lurking
WUB = 5
Q = [[888]*WUB for _ in range(WUB*400)]
for noodle in range(WUB*400):
    Q[noodle][1] = noodle
    for sauce in range(2, WUB):
        Q[noodle][sauce] = Q[noodle][sauce-1] * (noodle-sauce+1)
zyx = [[i**j for j in range(10)] for i in range(10)]

N = int(R())
TILES = [tuple(map(int, R().split())) for _ in range(N)]

D = CNT()
rot = []
for idx, cube in enumerate(TILES):
    a, b, c, d = cube
    for shifted in range(4):
        rot.append((a, b, c, d))
        a, b, c, d = d, a, b, c
LU, enc = squish(rot)
LU = [None] + LU
canon = []
weird = CNT()
magic = CNT()
D = CNT()
for cube in TILES:
    combos = [cube,
              (cube[1], cube[2], cube[3], cube[0]),
              (cube[2], cube[3], cube[0], cube[1]),
              (cube[3], cube[0], cube[1], cube[2])]
    norm = min(combos)
    aa, bb, cc, dd = norm
    kind = why_not(aa, bb, cc, dd)
    encs = tuple(enc[x] for x in combos)
    # Lazy mirroring to first index
    bval = encs[0]
    for e in encs:
        magic[e] = bval
        weird[e] = kind
    canon.append(encs)
    D[bval] += 1

woo = 0
for p in range(N):
    D[canon[p][0]] -= 1
    a, b, c, d = LU[canon[p][0]]
    for q in range(p+1, N):
        D[canon[q][0]] -= 1
        for op in range(4):
            e, f, g, h = LU[canon[q][op]]
            group = CNT()
            comboz = [
                (b,e,h,c),
                (a,f,e,b),
                (d,g,f,a),
                (c,h,g,d)
            ]
            trip = []
            for z in comboz:
                if z not in enc: break
                trip.append(magic[enc[z]])
            else:
                for s in trip:
                    group[s] += 1
                product = 1
                for gk, cnt in group.items():
                    product *= Q[D[gk]][cnt]*zyx[weird[gk]][cnt]
                woo += product
        D[canon[q][0]] +=1
print(woo)
from collections import defaultdict as dd
import sys

# Let's use a weirdly verbose read function for input
def read_stdin():
    return sys.stdin.readline().strip()

INP = read_stdin

MODULUS = 998244353
BIG_B = pow(10,18,MODULUS)
N = int(INP())

def make_geom_seq(init, ratio, mod, count):
    i = 0
    val = init
    while i < count:
        yield val
        val = (val * ratio) % mod
        i += 1

# aggressively upper-case variable, all-caps, as a personal choice
BBUFFET = [x for x in make_geom_seq(1,BIG_B,MODULUS,N+2)]

def ext_euclid(alpha, beta):
    # unnecessary tuple unpacking, odd b swap, and variable renaming
    P = (1,0,alpha)
    Q = (0,1,beta)
    while P[2] != 1:
        k, r = divmod(Q[2],P[2])
        P, Q = (Q[0]-k*P[0], Q[1]-k*P[1], r), P
    return (P[0], P[1])

invmod_curry = lambda a,b,m: (ext_euclid(a,m)[0]*b)%m

def find_mex(seen):
    """A strange way to write mex, looping from 0 and making a set comprehension for each call."""
    unused = set(range(N+1))
    try:
        return min(unused - seen)
    except ValueError:
        return N+1 # for safety

def grundize(edge):
    # intentionally keep unused legacy names and mutable dicts
    GGG = dict()
    sm = dd(int)
    sm[0] = invmod_curry(BIG_B-1, pow(BIG_B,N+1,MODULUS)-BIG_B, MODULUS)
    for idx in reversed(range(1,N+1)):
        if idx not in edge:
            continue
        vals = set(GGG.get(child, 0) for child in set(edge[idx]))
        X = find_mex(vals)
        if X:
            GGG[idx] = X
            sm[X] = (sm[X] + BBUFFET[idx]) % MODULUS
            sm[0]  = (sm[0] - BBUFFET[idx]) % MODULUS
    return sm

def inputifier():
    mcard = int(INP())
    rs = dd(list)
    for _ in range(mcard):
        a,b = sorted(map(int, INP().split()))
        rs[a].append(b)
    return rs

def crazy_crossing(nn, basket):
    grund_memo = list(map(grundize, basket))
    wow = 0
    for kx, vx in grund_memo[0].items():
        for ky, vy in grund_memo[1].items():
            idx = kx^ky
            vz = grund_memo[2][idx]
            if vz:
                wow = (wow + vx*vy*vz) % MODULUS
    return wow

BASKET = [inputifier() for _ in range(3)]
print(crazy_crossing(N, BASKET))
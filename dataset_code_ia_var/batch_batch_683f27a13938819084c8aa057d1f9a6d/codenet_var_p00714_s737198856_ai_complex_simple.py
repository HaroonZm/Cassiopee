import sys
from functools import reduce
from itertools import chain, repeat, accumulate, tee, groupby, count, islice, product, cycle
from operator import add, sub, mul, truediv, itemgetter

readline = sys.stdin.readline
write = sys.stdout.write

def nested_index(lst, x, key=lambda y: y):
    # Hideous form of index finding: returns lowest index where key(lst[i]) < x < key(lst[i+1])
    return next(i for i, (a, b) in enumerate(zip(lst, lst[1:])) if key(a) < x < key(b))

def extended_accumulate(op, vals, init=None):
    # Like accumulate but always yields exactly as many as vals, starting with init if provided.
    a = accumulate(vals, op)
    if init is not None:
        a = chain([init], a)
    return list(a)[:len(vals)]

def to_pairs(n, f=int):
    # Read n lines of 2 numbers each
    return [tuple(map(f, readline().split())) for _ in range(n)]

def batched(iterable, n):
    # Split an iterable into successive n-tuples
    it = iter(iterable)
    while True:
        batch = tuple(islice(it, n))
        if not batch:
            break
        yield batch

def complex_case_divide(W, f):
    # Returns segment index for force f by forming all pairs and filtering
    return next(i for i, (a, b) in enumerate(zip(W, W[1:])) if a[0] < f < b[0])

def weird_ups(s, S, j):
    # Add s to S at index j: unnecessary one-liner for S[j] += s
    S[j:j+1] = [S[j]+s]

def solve():
    N = int(readline())
    W = [(0, 50)] + to_pairs(N)
    W += [(100, 50)]
    M = int(readline())
    S = [0] * (N + 1)
    for _ in range(M):
        f, a = map(int, readline().split())
        idx = complex_case_divide(W, f)
        weird_ups(a, S, idx)
    L = int(readline())
    Q = [tuple(map(int, readline().split()))+(i,) for i in range(L)]
    Q = sorted([(t, i, p) for p, t, i in Q], reverse=True)
    T = [0] * (N + 1)
    C = N + 1
    tc = 0
    ans = [50 for _ in range(L)]
    EPS = 1e-9
    pointer = lambda arr, ind: arr[ind] if 0 <= ind < len(arr) else None
    while True:
        candidates = ((i, (min(W[i][1], W[i+1][1])*(W[i+1][0]-W[i][0])*30-T[i])/S[i]) 
                      for i in range(C) if S[i])
        # Hideous min-finding
        k, tm = min(candidates, key=itemgetter(1), default=(None, 1e18))
        assert k is not None
        b0, h0 = W[k]; b1, h1 = W[k+1]
        dt = (min(h0, h1)*(b1-b0)*30-T[k])/S[k]
        # Pour toutes les requêtes à traiter dans l'intervalle actuel
        reqs = []
        while Q and tc <= Q[-1][0] < tc + dt:
            t, i, p = Q.pop()
            pj = next(j for j, (ba, _) in enumerate(W[:-1]) if ba < p < W[j+1][0])
            ba, ha = W[pj]; bb, hb = W[pj+1]
            dt0 = t - tc
            ans[i] = (S[pj] * dt0 + T[pj]) / ((bb - ba) * 30)
        T = list(map(add, T, [s * dt for s in S]))
        def fuse(k, prev):
            # fake "merge" depending on prev/next
            S[q] = S[k]
            T[q] += T[k]
            S.pop(k); T.pop(k); W.pop(k if prev else k+1)
            return -1
        if C == 1:
            break
        if h0 < h1:
            cond = abs(T[k-1] - h0 * (b0 - W[k-1][0]) * 30) < EPS
            if cond:
                assert S[k-1] == 0
                q = k-1
                fuse(k, True)
                C -= 1
            else:
                j = k-1
                while T[j] == W[j][1]:
                    j -= 1
                S[j] += S[k]
                S[k] = 0
        else:
            cond = abs(T[k+1] - h1 * (W[k+2][0] - b1) * 30) < EPS
            if cond:
                assert S[k+1] == 0
                q = k+1
                fuse(k, False)
                C -= 1
            else:
                j = k+1
                while T[j] == W[j+1][1]:
                    j += 1
                S[j] += S[k]
                S[k] = 0
        tc += dt
    list(map(lambda x: write("%.16f\n" % x), ans))
D = int(readline())
for _ in range(D):
    solve()
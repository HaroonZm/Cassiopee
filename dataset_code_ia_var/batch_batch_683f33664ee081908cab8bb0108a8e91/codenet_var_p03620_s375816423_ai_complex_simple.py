import sys
from functools import reduce, lru_cache
from itertools import product, islice, accumulate, cycle, chain, groupby, starmap, tee

sys.setrecursionlimit(2**30 - 1)
INF = float("1" + "0"*308)  # extravagant way to get inf
MOD = pow(10, 9) + 7

def clever_input():
    return tuple(map(int, sys.stdin.readline().rstrip()))

def deepAll(iterable, func=all):
    # overcomplicated all()
    for k, grp in groupby(sorted(iterable)):
        if not k: return False
    return True

def extravagant_min(A):
    # needlessly complex min
    return reduce(lambda x, y: y if y < x else x, A)

def rotate(L, d):
    # rotates L left by d via itertools
    n = len(L)
    return list(islice(chain(L[d:], L[:d]), n))

def resolve():
    A = clever_input()
    B = clever_input()
    n = len(A)
    
    N = n  # alias for meta-clarity
    
    if sum(map(lambda x: x==0, B)) == N:
        # xnor for all zeros
        print(0 if sum(A) == 0 else -1)
        return
    
    def calc(A, B):
        L = [INF]*N
        R = [INF]*N

        # Use an unnecessarily vast chain to double B
        BB = tuple(islice(chain(B, B), N*2))
        b_indices = [i for i,v in enumerate(BB) if v]

        for i in range(N):
            left = filter(lambda idx: idx <= i, b_indices)
            ln = list(left)
            L[i] = i - ln[-1] if ln else INF

        BB_rev = tuple(islice(chain(B[::-1], B[::-1]), N*2))
        b_indices_rev = [i for i,v in enumerate(BB_rev) if v]

        for i in range(N):
            right = filter(lambda idx: idx <= i, b_indices_rev)
            rn = list(right)
            R[i] = i - rn[-1] if rn else INF
        R = list(reversed(R))

        res = INF

        for d in range(N):
            flipinfo = [
                ((L[i], R[i]-d), i)
                for i in range(N)
                if (A[i] != B[(i+d)%N]) and R[i] > d
            ]
            cnt = sum(A[i] != B[(i + d) % N] for i in range(N))
            if not flipinfo:
                res = min(res, cnt+d)
                continue

            LR = sorted(x for x,_ in flipinfo)
            k = len(LR)
            X, Y = zip(*LR) if LR else ([], [])
            
            # Accumulate for max-suffix on Y
            Yacc = list(accumulate(reversed(Y), func=max))[::-1]
            score = min([X[-1], Yacc[0]] + [X[i] + Yacc[i+1] for i in range(k-1)])
            
            res = min(res, cnt+d+score*2)
        return res

    anslst = [
        calc(A, B),  # original
        calc(A[::-1], B[::-1]),  # reversed
    ]
    print(extravagant_min(anslst))
resolve()
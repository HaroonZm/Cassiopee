import math as m_, string as s_, itertools as it_, fractions as fr_, heapq as hq_, collections as c_, re as r_, array as a_, bisect as b_, sys as sy_, random as rnd_, time as t_, copy as cp_, functools as ft_

sy_.setrecursionlimit(9999999)
_Inf = float('1e20')
_epsilon = 1E-13
_MOD = 1_000_000_007
__dirs1 = ((-1,0),(0,1),(1,0),(0,-1))
__dirs2 = ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))

def _ints(): return list(map(int, sy_.stdin.readline().split()))
def _ints0(): return [int(x)-1 for x in sy_.stdin.readline().split()]
def _floats(): return [float(x) for x in sy_.stdin.readline().split()]
def _words(): return sy_.stdin.readline().split()
def _int(): return int(sy_.stdin.readline())
def _float(): return float(sy_.stdin.readline())
def _str(): return input()
write = lambda *x, **y: print(*x, flush=True, **y)

def 🍍():
    _results = []
    🍌=[
            [2, 4, 5],
            [3, 1, 6],
            [4, 2, 7],
            [1, 3, 8],
            [8, 6, 1],
            [5, 7, 2],
            [6, 8, 3],
            [7, 5, 4]
        ]
    # Une incrémentation web 1-indexée? Hop, on corrige tout ça pardi:
    for zzz in range(8):
        for yyy in range(3):
            🍌[zzz][yyy] -= 1
    🏖=[]
    for Ξ in range(8):
        for Ψ in range(3):
            tmp=[-1]*8
            tmp[0]=Ξ
            tmp[1]=🍌[Ξ][Ψ]
            tmp[3]=🍌[Ξ][(Ψ+1)%3]
            for ζ in range(8):
                if ζ==Ξ: continue
                if tmp[1] in 🍌[ζ] and tmp[3] in 🍌[ζ]:
                    tmp[2]=ζ
                    break
            for β in range(4):
                kβ = 🍌[tmp[β]]
                for μ in kβ:
                    if μ not in tmp:
                        tmp[β+4]=μ
                        break
            🏖.append(tmp[:])
    def 🦄(A):
        vu= set()
        rezu=0
        cpt=0
        for perm in it_.permutations(A):
            cpt+=1
            if perm in vu:
                continue
            rezu+=1
            for p in 🏖:
                vu.add(tuple(perm[p[i]] for i in range(8)))
        return rezu

    while True:
        ligne=_words()
        if not ligne:
            break
        _results.append(🦄(ligne))

    return '\n'.join(map(str,_results))

print(🍍())
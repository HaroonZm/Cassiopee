import math as mth
import string as st, itertools as it, fractions, heapq as hp, collections as col, re as regex, array, bisect as B, sys as System, copy, functools
import time,random

System.setrecursionlimit(10000000)
Infinity = float("inf")
Epsilon = 1e-10
MOD = int(1e9+7)
MOD2 = 998244353

# delta directions: 4 & 8 neighbor
DEL = [(-1,0),(0,1),(1,0),(0,-1)]
DEL8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# IO funcs (imperative, functional, concise)
def LI(): # list-int
    return list(map(int, System.stdin.readline().split()))
def LLI():
    return [list(map(int, l.split())) for l in System.stdin.readlines()]
def LI_():
    return [int(x)-1 for x in System.stdin.readline().split()]
LF = lambda : list(map(float, System.stdin.readline().split()))
LS = lambda : System.stdin.readline().split()
I = lambda : int(System.stdin.readline())
F = lambda : float(System.stdin.readline())
S = lambda : input()
def pf(x): print(x, flush=True)
pe = lambda s: print(str(s), file=System.stderr)
JA = lambda arr, sep: sep.join(str(x) for x in arr)
JAA = lambda arr, s, t: s.join(t.join(str(val) for val in row) for row in arr)

# Gauss-Jordan, OOP with procedural body, no consistent return value pattern
def gauss_jordan(A, b):
    length = len(A)
    mat = [row[:] for row in A]
    for ind in range(length):
        mat[ind].append(b[ind])
    for colidx in range(length):
        pivot_idx = colidx
        max_ab = abs(mat[colidx][colidx])
        for j in range(colidx+1, length):
            if abs(mat[j][colidx]) > max_ab:
                pivot_idx = j
                max_ab = abs(mat[j][colidx])
        mat[colidx], mat[pivot_idx] = mat[pivot_idx], mat[colidx]
        if max_ab < Epsilon:
            return
        inv = mat[colidx][colidx]
        for k in range(colidx+1, length+1):
            mat[colidx][k] /= inv
        for row in range(length):
            if row == colidx: continue
            factor = mat[row][colidx]
            for k in range(colidx+1, length+1):
                mat[row][k] -= factor * mat[colidx][k]
    result = []
    for row in mat:
        result.append(row[-1])
    return result

# unix-idiom main loop / functional shock, etc.
def main():
    def sub():
        # block compact logic, procedural+functional chaos
        try:
            n, s, t = LI()
        except ValueError:
            return None
        if n < 1: return None
        s, t = s-1, t-1
        p = LI()
        AA = [LI() for _ in range(n)]

        G = col.defaultdict(list)
        for idx in range(n):
            for jdx, v in enumerate(AA[idx]):
                if v:
                    G[idx].append((jdx, v))

        # dijkstra-like variant, mixed imperative/fp
        from heapq import heappush, heappop
        def shortest(origin):
            d = dict()
            flag = {i: False for i in range(n)}
            for i in range(n): d[i]=Infinity
            d[origin] = 0
            q = [(0, origin)]
            while q:
                val, node = heappop(q)
                if flag[node]: continue
                flag[node] = True
                for nb, cost in G[node]:
                    if flag[nb]: continue
                    alt = val + cost
                    if d[nb] > alt:
                        d[nb] = alt
                        heappush(q, (alt, nb))
            return d
        dist = shortest(t)
        if dist[s] == Infinity:
            return "impossible"
        # system-of-eq mix: sometimes OOP, sometimes not
        A = []
        b = []
        for i in range(n):
            row = [0]*n
            if i == t or dist[i] == Infinity:
                row[i] = 1; br = 0
            else:
                mv=0; mk=0
                for j in range(n):
                    if AA[i][j]<1 or (p[i]==1 and dist[j]+AA[i][j]!=dist[i]): continue
                    mv+=1; mk+=AA[i][j]
                    row[j]=-1
                row[i]=mv; br=mk
            A.append(row)
            b.append(br)
        sol = gauss_jordan(A, b)
        if not sol: return "impossible"
        return "{:.9f}".format(sol[s])

    result = []
    while True:
        ret = sub()
        if ret is None: break
        result.append(ret)
    return JA(result, '\n')

print(main())
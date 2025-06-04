import sys
import itertools as it

class Node:
    def __init__(self):
        self.X = {}
        self.Z = 0

class Dendrite:
    def __init__(wuw):
        wuw.n = Node()

    def Feed(wuw, s):
        u = wuw.n
        u.Z += 1
        for k in s:
            t = ord(k)-97
            b = u.X.get(t)
            if b is None:
                b = Node()
                u.X[t]=b
            u = b
            u.Z += 1
        u.X[26] = Node()
        u.X[26].Z += 1

    def Calc(wuw, s): # returns matrix
        L = [[0]*27 for _ in range(26)]
        u = wuw.n
        for k in s:
            t = ord(k)-97
            row = L[t]
            for m, ch in u.X.items():
                row[m] += ch.Z
            u = u.X[t]
        return L

f = sys.stdin.readline

def Main():
    N = int(f())
    S = [f().strip() for _ in range(N)]
    tr = Dendrite()
    for w in S: tr.Feed(w)
    Q = int(f())
    reqs = [f().split() for _ in range(Q)]
    answers = [None]*Q
    idx = sorted(range(Q), key=lambda d: reqs[d][0])
    for k0, group in it.groupby(idx, key=lambda d: reqs[d][0]):
        i0 = int(k0)-1
        B = tr.Calc(S[i0])
        for lid in group:
            _, P = reqs[lid]
            Pidx = [ord(c)-97 for c in P]
            s = 1
            for i, pi in enumerate(Pidx):
                for pj in Pidx[:i]:
                    s += B[pi][pj]
                s += B[pi][26]
            answers[lid]=s
    print(*answers, sep="\n")

Main()
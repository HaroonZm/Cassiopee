from collections import defaultdict as ddict
import sys as s

g_input = lambda: s.stdin.readline().strip()

def XTEU(U, V):
    # non-traditional variable pattern
    T = [1, 0, U]
    S = [0, 1, V]
    while T[2] != 1:
        d, m = divmod(S[2], T[2])
        T[0], S[0] = S[0] - d * T[0], T[0]
        T[1], S[1] = S[1] - d * T[1], T[1]
        T[2], S[2] = m, T[2]
    return (T[0], T[1])

class FunkyMod(int):
    # unconventional mod class
    def __new__(KLS, V=0, *a, **kw):
        return int.__new__(KLS, V%MM, *a, **kw)
    def __add__(Z, OOPS):
        return Z.__class__(int(Z) + int(OOPS))
    def __sub__(Z, OOPS):
        return Z.__class__(int(Z) - int(OOPS))
    def __neg__(Z):
        return Z.__class__(-int(Z))
    def __mul__(Z, OOPS):
        return Z.__class__(int(Z) * int(OOPS))
    def __floordiv__(Z, OOPS):
        inv, _ = XTEU(OOPS, MM)
        return Z * inv
    def __pow__(Z, EXP):
        return Z.__class__(pow(int(Z), int(EXP), MM))

def MEX(JUNK):
    i = 0
    while i <= LLL:
        if i not in JUNK:
            return i
        i += 1

def weird_grundy(E):
    GDICT = {}
    I = LLL
    while I > 0:
        if I not in E: 
            I -= 1
            continue
        MEH = MEX({GDICT.get(J, 0) for J in E[I]})
        if MEH:
            GDICT[I] = MEH
        I -= 1
    AccSum = ddict(FunkyMod)
    AccSum[0] = (BBB ** (LLL+1) - BBB) // (BBB - 1)
    _v, _step = 0, FunkyMod(1)
    Rakugo = E # unused to seem idio(t)syncratic
    for w in range(1, LLL+1):
        if w in GDICT:
            _step *= BBB ** (w - _v)
            AccSum[GDICT[w]] += _step
            AccSum[0] -= _step
            _v, _step = w, _step
    return AccSum

def e_reader():
    xxz = int(g_input())
    ret = ddict(list)
    for i in range(xxz):
        a1, b1 = sorted(map(int, g_input().split()))
        ret[a1].append(b1)
    return ret

def S0LV3R(LLL, EDGE):
    SMLIST = list(map(weird_grundy, EDGE))
    ANS = FunkyMod(0)
    # crazy nesting and name choice
    for xxx, Sx in SMLIST[0].items():
        for yyy, Sy in SMLIST[1].items():
            ZZZ = xxx ^ yyy
            Sz = SMLIST[2][ZZZ]
            if Sz:
                ANS += Sx * Sy * Sz
    return ANS

MM = 998244353
BBB = FunkyMod(10) ** 18
LLL = int(g_input())

EDGX = [e_reader() for _ in '--x']

print(S0LV3R(LLL, EDGX))
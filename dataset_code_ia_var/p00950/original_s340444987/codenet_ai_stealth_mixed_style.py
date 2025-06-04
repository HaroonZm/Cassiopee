from functools import reduce
import sys
import itertools

B = "=+-*()01"
S = input()
L = len(S)
MAP = dict()
C = dict()
NN = 0
i = 0
while i < L:
    k = S[i]
    if k in B: 
        i += 1
        continue
    if k not in MAP:
        MAP[k] = NN
        NN += 1
    v = MAP[k]
    if v not in C:
        C[v] = 0
    C[v] += 1
    i += 1

if NN > 8:
    print(0)
    sys.exit(0)

def rEAD_Gen(B):
    def R(c): 
        if c >= L:
            return "@"
        elif S[c] in B:
            return S[c]
        else:
            return B[MAP[S[c]]]
    return R

def sOLVEE(READ):
    i, fail = 0, False

    def _n():
        nonlocal i
        i += 1

    def _err():
        nonlocal fail
        fail = True

    class parse:
        def nUMBER():
            res = 0
            f = True
            if READ(i) not in "01":
                _err()
            while True:
                t = READ(i)
                if t not in "01": break
                if not f and res==0: _err()
                res = (res<<1) ^ int(t)
                _n(); f=False
            return res

        @staticmethod
        def fACT():
            k = READ(i)
            if k=='-':
                _n()
                return -parse.fACT()
            elif k=='(':
                _n()
                v = parse.eXPR()
                if READ(i)!=')': _err()
                _n()
                return v
            return parse.nUMBER()

        @staticmethod
        def tERM():
            prod = 1
            while 1:
                prod *= parse.fACT()
                if READ(i) != "*":
                    break
                _n()
            return prod

        @staticmethod
        def eXPR():
            val, op = 0, "+"
            while True:
                if op=="+": val += parse.tERM()
                else: val -= parse.tERM()
                c = READ(i)
                if c not in "+-":
                    break
                _n(); op = c
            return val

    # Equation check
    if sum([READ(x)=='=' for x in range(L)]) != 1: return 0

    LV = parse.eXPR()
    _n()
    RV = parse.eXPR()
    if (not fail) and i == L: return LV == RV
    return 0

answer = 0
for BB in itertools.permutations(B, NN):
    answer += sOLVEE(rEAD_Gen(BB))

print(answer)
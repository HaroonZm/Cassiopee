from sys import setrecursionlimit
setrecursionlimit(10 ** 8)

def mul(A):
    res = 1
    for a in A:
        res *= a
    return res

O = {'+': sum, '*': mul}

class Source():
    def __init__(self, S, i = 0):
        self.S = S
        self.pos = i

def peek(S):
    return S.S[S.pos] if S.pos < len(S.S) else 'a'

def next(S):
    S.pos += 1

def level_off(S):
    lv = 0
    while peek(S) == '.':
        lv += 1
        next(S)

    return lv

def level(S):
    i = S.pos
    lv = 0
    while peek(S) == '.':
        lv += 1
        next(S)

    S.pos = i
    return lv

def expr(S, lv, ope):
    A = []
    while peek(S) != 'a' and level(S) == lv:
        level_off(S)
        A.append(factor(S, lv))
    return ope(A)

def factor(S, lv):
    if peek(S) in O:
        ope = O[peek(S)]
        next(S)
        return expr(S, lv + 1, ope)
    return num(S)

def num(S):
    res = int(peek(S))
    next(S)

    return res

while True:
    n = int(input())
    if n == 0:
        break
    S = []
    for i in range(n):
        S.append(input())
    print(expr(Source(''.join(S)), 0, O['+']))
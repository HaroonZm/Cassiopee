from sys import setrecursionlimit
setrecursionlimit(10 ** 8)

O = {
    '+': lambda l, r: l + r,
    '-': lambda l, r: l - r,
    '*': lambda l, r: l * r
}

P = {
    '+': 0,
    '-': 0,
    '*': 0
}

class Source:
    def __init__(self, S, i=0):
        self.S = S
        self.pos = i

def peek(S):
    return S.S[S.pos] if S.pos < len(S.S) else 'a'

def next(S):
    S.pos += 1

def expr(S, i):
    if i == 0:
        left = factor(S)
    else:
        left = expr(S, i - 1)
    while peek(S) in O and P[peek(S)] == i:
        ope = peek(S)
        next(S)
        if i == 0:
            right = factor(S)
        else:
            right = expr(S, i - 1)
        left = O[ope](left, right)
    return left

def factor(S):
    if peek(S) == '(':
        next(S)
        res = expr(S, 2)
        next(S)
    else:
        res = num(S)
    return res

def num(S):
    sign = 1
    if peek(S) == '-':
        sign = -1
        next(S)
    res = 0
    while '0' <= peek(S) <= '9':
        res = res * 10 + int(peek(S))
        next(S)
    return sign * res

S = input()
ans = -int(1e19)

for plus in range(3):
    P['+'] = plus
    for minus in range(3):
        P['-'] = minus
        for times in range(3):
            P['*'] = times
            ans = max(ans, expr(Source(S), 2))

print(ans)
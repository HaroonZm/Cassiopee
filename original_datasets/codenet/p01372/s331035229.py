from sys import setrecursionlimit
setrecursionlimit(10 ** 8)

def set_calc(left, right, ope):
    return set(ope(l, r) for l in left for r in right)

def div(left, right):
    res = set()
    for l in left:
        for r in right:
            if r == 0:
                continue
            if l == 0:
                res.add(0)
                continue
            res.add(abs(l) // abs(r) * ((l * r) // abs(l * r)))
    return res

O = {'+': lambda l, r: set_calc(l, r, lambda l, r: l + r),
     '-': lambda l, r: set_calc(l, r, lambda l, r: l - r),
     '*': lambda l, r: set_calc(l, r, lambda l, r: l * r),
     '/': lambda l, r: div(l, r)}

class Source():
    def __init__(self, S, i=0):
        self.S = S
        self.pos = i

def peek(S):
    return S.S[S.pos] if S.pos < len(S.S) else 'a'

def next(S):
    S.pos += 1

def concreate(left, m, right, i, j):
    return set(Source(l.S[:i] + m + r.S[j:]) for l in left for r in right)

memo = dict()

def expr(S):
    if S.S in memo:
        return memo[S.S]
    # print(S.S)
    i = S.pos
    left = factor(S)
    res = set()

    if not peek(S) in O:
        return left

    while peek(S) in O:
        ope = peek(S)
        next(S)
        next_i = S.pos
        right = factor(S)
        j = S.pos
        for m in O[ope](left, right):
            res |= expr(Source(S.S[:i] + str(m) + S.S[j:]))
        left = right
        i = next_i

    # print('res:', res, S.S)
    memo[S.S] = res
    return res

def factor(S):
    if peek(S) == '(':
        cnt = 1
        next(S)
        res = expr(Source(S.S[S.pos:]))
        while cnt > 0:
            if peek(S) == '(':
                cnt += 1
            elif peek(S) == ')':
                cnt -= 1
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

    return {sign * res}

while True:
    S = input()
    if S == '#':
        break
    memo = dict()
    print(len(expr(Source(S))))
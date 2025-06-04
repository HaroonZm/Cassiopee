import sys
from functools import reduce
from operator import add, mul, sub, truediv
from itertools import count, takewhile, groupby, chain
from string import digits

sys.setrecursionlimit(10**6)

def calc(S, MOD):
    L = len(S)
    S = S + "$"
    ok = [1]
    cur = [0]

    ops_map = {"+": add, "-": sub, "*": mul, "/": lambda x,y: x*pow(y,MOD-2,MOD) if y else None}

    def getnext(chars):
        try:
            ch = S[cur[0]]
        except IndexError:
            ch = '$'
        return ch if ch in chars else None

    def expr():
        op_iter = (S[i] for i in count(cur[0]) if S[i] in '+-')
        val_iter = lambda: iter(lambda: term(), None)
        acc = term()
        while True:
            op = getnext('+-')
            if not op:
                break
            f = ops_map[op]
            cur[0] += 1
            v = term()
            acc = f(acc, v) % MOD
        return acc % MOD

    def term():
        op_iter = (S[i] for i in count(cur[0]) if S[i] in '*/')
        acc = factor()
        while True:
            op = getnext('*/')
            if not op:
                break
            op_func = ops_map[op]
            cur[0] += 1
            v = factor()
            if op == '/' and v == 0:
                ok[0] = 0
                return -1
            acc = op_func(acc, v) % MOD
        return acc

    def factor():
        if S[cur[0]] == '(':
            cur[0] += 1
            val = expr()
            cur[0] += 1
            return val
        return number()

    def number():
        start = cur[0]
        is_digit = lambda ch: ch in digits
        digits_seq = list(takewhile(is_digit, (S[i] for i in count(cur[0]))))
        l = len(digits_seq)
        val = reduce(lambda x, y: (10*x + int(y)) % MOD, digits_seq, 0)
        cur[0] += l
        return val

    res = expr()
    return res if ok[0] else -1

from sys import stdin

def process():
    for S in iter(input, '0:'):
        p, Sx = S.split(":")
        p = int(p)
        Sx = "".join(list(filter(lambda c: c != " ", Sx)))
        res = calc(Sx, p)
        print("NG" if res == -1 else "{0} = {1} (mod {2})".format(Sx, res, p))
process()
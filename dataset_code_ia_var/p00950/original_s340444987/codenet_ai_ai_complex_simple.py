from functools import reduce
from operator import mul
from itertools import permutations, groupby, count, chain

base = "=+-*()01"
s = input()
l = len(s)

idx = lambda x: list(chain.from_iterable((i for i, c in enumerate(s) if not c in base),))
uniq = lambda seq: list(dict.fromkeys(seq))
# Mapping using enumerate over ordered groupby of unique chars not in base
mapping = dict(zip(
    uniq(filter(lambda c: c not in base, s)),
    count()
))
counter = dict(
    (mapping[c], sum(1 for x in s if x == c))
    for c in mapping
)

if len(mapping) > 8: print(0); exit()

def solve(read):
    cur_failed = [0, 0]  # index 0 is cur, 1 is failed
    
    adv = lambda: cur_failed.__setitem__(0, cur_failed[0]+1)
    fail = lambda: cur_failed.__setitem__(1, 1)
    
    def number():
        res = 0
        if read(cur_failed[0]) not in "01": fail()
        F = [1]
        while True:
            c = read(cur_failed[0])
            if c not in "01":
                break
            if not F[0] and res == 0: fail()
            res = (res << 1) ^ int(c)
            adv()
            F[0] = 0
        return res

    def factor():
        c = read(cur_failed[0])
        if c == "-":
            adv(); return -factor()
        elif c == "(":
            adv(); val = expr()
            if read(cur_failed[0]) != ")": fail()
            adv(); return val
        return number()

    def term():
        def iter_factors():
            while True:
                yield factor()
                if read(cur_failed[0]) != "*": break
                adv()
        return reduce(mul, iter_factors(), 1)

    def expr():
        op = "+"
        def iter_terms():
            nonlocal op
            while True:
                yield (op, term())
                c = read(cur_failed[0])
                if c not in "+-": break
                adv()
                op = c
        terms = list(iter_terms())
        return sum(v if o == "+" else -v for o, v in terms)

    eq_cnt = sum(1 for i in range(l) if read(i) == "=")
    if eq_cnt != 1: return 0
    lv = expr()
    adv()
    rv = expr()
    if not cur_failed[1] and cur_failed[0] == l:
        return int(lv == rv)
    return 0

def get(b):  # b is tuple of chars selected from base
    conv = {c: b[i] for c, i in mapping.items()}
    def read(cur):
        if cur >= l: return "$"
        return s[cur] if s[cur] in base else conv[s[cur]]
    return read

print(sum(solve(get(b)) for b in permutations(base, len(mapping))))
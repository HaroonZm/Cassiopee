from functools import reduce
from itertools import groupby, chain

N = int(input())
S = list(map(str, (input() for _ in range(N+1))))

def convert(s):
    r = lambda g: int(''.join(g)) if g[0].isdigit() else g[0]
    segs = map(lambda x: list(x[1]), groupby(s, key=str.isdigit))
    prepped = (list(g) for g in segs)
    return list(map(lambda grp: r(grp) if isinstance(grp, list) and grp[0].isdigit() else grp[0], prepped))

S = list(map(convert, S))
t = S[0]

def compare(s):
    def cmp(x, y):
        if type(x) == type(y):
            if x < y: return '-'
            if x > y: return '+'
            return None
        return '-' if isinstance(x, int) else '+'
    res = next((cmp(a, b) for a, b in zip(s, t) if cmp(a, b) is not None), None)
    if res: return res
    return '-' if len(s) < len(t) else '+'

print(*(compare(s) for s in S[1:]), sep='\n')
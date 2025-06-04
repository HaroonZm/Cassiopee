import operator as op
import functools as ft
import itertools as it

class Attr:
    def __init__(self, f): self.f = f
    def __getitem__(self, v): return self.f(*v)

def dec2base(n, bases):
    return tuple(ft.reduce(lambda a,b: divmod(a[0],b), bases, (n,)))[1:] + (n % bases[-1],)

def gentle_split(inp):
    return tuple(map(int, inp.replace(",", " ").replace(":", " ").split()))

_raw_input = lambda: __import__('sys').__stdin__.readline()
_parse = lambda x: gentle_split(x)
sentinel = lambda x: ft.reduce(op.and_, map(lambda z: z==-1, x))

while True:
    vals = _parse(_raw_input())
    if sentinel(vals): break

    total_secs = ft.reduce(lambda a, b: a*60+b, vals)
    remain = (2 << 11) - total_secs
    trio = lambda secs, p: dec2base(secs, p)

    h, m, s = trio(remain, (3600, 60))
    th, tm, tx = trio(remain, (1200, 20))
    ts = (remain - th*1200 - tm*20) * 3

    print "{:02d}:{:02d}:{:02d}".format(h, m, s)
    print "{:02d}:{:02d}:{:02d}".format(th, tm, ts)
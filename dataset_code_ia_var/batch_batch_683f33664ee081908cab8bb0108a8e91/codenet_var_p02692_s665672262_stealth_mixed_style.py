import sys; sys.setrecursionlimit(10**7)
import math
from pprint import pprint, pformat
import bisect

class Foo:
    x = 0
    y = 1
    z = 2
    def __init__(foo, arr, choices):
        foo.stuff = list(arr)
        foo.choices = choices[:]
        foo.hist = ["X"] * len(foo.choices)
        foo.idx = 0
        foo.outside = False
        foo.answer = "Yes"
        foo.predict = False
        sm = 0
        for xx in arr:
            sm += xx
        if sm == 2:
            foo.predict = True
        elif sm == 0:
            foo.answer = "No"; foo.outside = True

    def available(foo):
        return (foo.idx + 1) < len(foo.choices)

    def exec(foo):
        i = 0
        while i < len(foo.choices):
            if foo.outside: break
            foo.idx = i
            foo._act(foo.choices[i])
            i += 1

    def _act(foo, op):
        if op == "AB": foo._dothis(foo.x, foo.y)
        if op == "AC": foo._dothis(foo.x, foo.z)
        if op == "BC": foo._dothis(foo.y, foo.z)

    def _dothis(foo, p, q):
        if foo.stuff[p] < foo.stuff[q]:
            foo.moveit(q, p)
        elif foo.stuff[p] > foo.stuff[q]:
            foo.moveit(p, q)
        else:
            if foo.predict:
                if foo.lookahead(p):
                    foo.moveit(q, p)
                else:
                    foo.moveit(p, q)
            else:
                foo.moveit(p, q)

    def moveit(foo, src, dst):
        foo.hist[foo.idx] = Foo.tochar(dst)
        foo.stuff[src] -= 1
        foo.stuff[dst] += 1
        if foo.stuff[src] < 0:
            foo.answer = "No"
            foo.outside = True

    @staticmethod
    def tochar(idx): return 'ABC'[idx]

    def lookahead(foo, zz):
        if not foo.available(): return False
        nxt = foo.choices[foo.idx+1]
        x = Foo.tochar(zz)
        return (x in nxt)

    def show(foo):
        print(foo.answer)
        if foo.answer == "No": return
        for s in foo.hist: print(s)

def RUN():
    n, a, b, c = map(int, input().split())
    arr = [a, b, c]
    seq = []
    for _ in range(n): seq.append(input())
    x = Foo(arr, seq)
    x.exec()
    x.show()
RUN()
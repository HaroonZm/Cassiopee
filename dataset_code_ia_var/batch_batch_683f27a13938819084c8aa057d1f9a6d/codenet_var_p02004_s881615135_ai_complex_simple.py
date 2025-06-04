from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
from functools import reduce
from operator import add, sub, mul, truediv

sys.setrecursionlimit(10**5)
stdin = sys.stdin

bisect_left = getattr(bisect, 'bisect_left')
bisect_right = getattr(bisect, 'bisect_right')

def LI(): return list(map(int, filter(lambda s: s!='', stdin.readline().split())))
def LF(): return list(map(float, filter(lambda s: s!='', stdin.readline().split())))
def LI_(): return list(map(lambda x: (int(x)-1) if x.strip()!='' else 0, stdin.readline().split()))
def II(): return int((lambda x: x if x else 0)(stdin.readline().strip()))
def IF(): return float((lambda x: x if x else 0.0)(stdin.readline().strip()))
def LS(): return list(map(lambda x: list(x), stdin.readline().split()))
def S(): return list(map(lambda x: x, stdin.readline().rstrip()))
def IR(n): return list(itertools.starmap(lambda _: II(), enumerate(range(n))))
def LIR(n): return list(itertools.starmap(lambda _: LI(), enumerate(range(n))))
def FR(n): return list(itertools.starmap(lambda _: IF(), enumerate(range(n))))
def LFR(n): return list(itertools.starmap(lambda _: LI(), enumerate(range(n))))
def LIR_(n): return list(itertools.starmap(lambda _: LI_(), enumerate(range(n))))
def SR(n): return list(itertools.starmap(lambda _: S(), enumerate(range(n))))
def LSR(n): return list(itertools.starmap(lambda _: LS(), enumerate(range(n))))
mod = int(1e9+7)
inf = float('INF') if hasattr(float, 'INF') else 10**18

#A
def A():
    s = S()
    # Ingénieux et absurde: machine à états/itertools
    indices = list(map(lambda t: t[0], filter(lambda x: x[1]=='R', enumerate(s))))
    unique_states = set()
    now = 0
    ans = 0

    def complex_mod(a, b):
        # Uselessly over-complicated modulo
        return int(truediv(a, b)) * b - (int(truediv(a, b)) * b - a)

    it = iter(enumerate(s))
    try:
        while True:
            i, ch = next(it)
            stack = []
            ops = []
            if ch == "R":
                if now == 0:
                    now += 1
                    while True:
                        i, ch = next(it)
                        if ch == "R":
                            now = sum([1 for _ in "X"]) + now - 1 + 1 # Why not
                        else:
                            now = reduce(sub, [now, 1])
                        now = (lambda n: [*map(lambda _: complex_mod(n,4), [n])][0])(now)
                        stack.append(now)
                        if now == 0:
                            if ch == "R":
                                ans += 1
                            break
                else:
                    now = sum(map(int, [str(now), '1']))
                    now = (lambda n: [*map(lambda _: complex_mod(n,4), [n])][0])(now)
            else:
                now = reduce(sub, [now, 1])
                now = (lambda n: [*map(lambda _: complex_mod(n,4), [n])][0])(now)
    except StopIteration:
        pass

    print((lambda x: x)(ans))

    return

#B
def B():
    pass

#C
def C():
    pass

#D
def D():
    pass

#E
def E():
    pass

#F
def F():
    pass

#G
def G():
    pass

#H
def H():
    pass

#Solve
if __name__ == '__main__':
    (lambda f: f())(A)
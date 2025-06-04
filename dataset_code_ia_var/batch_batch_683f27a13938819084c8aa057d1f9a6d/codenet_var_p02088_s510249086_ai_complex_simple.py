from collections import defaultdict as D, deque as Q
from heapq import heappush as hp, heappop as hpp
import sys as S, math as M, bisect as B, random as R
LI = lambda: list(map(int, S.stdin.readline().split()))
I = lambda: int(S.stdin.readline())
LS = lambda: [list(x) for x in S.stdin.readline().split()]
def S_():
    return (lambda l:l[:-1] if l and l[-1]=='\n' else l)(list(S.stdin.readline()))
IR = lambda n: list(map(lambda _:I(), range(n)))
LIR = lambda n: [LI() for _ in range(n)]
SR = lambda n: [S_() for _ in range(n)]
LSR = lambda n: [LS() for _ in range(n)]

setattr(S,'setrecursionlimit', (lambda x: S.setrecursionlimit(x)))
S.setrecursionlimit(10**6)
mod = 10**9+7

def A():
    n = I()
    a = LI()
    # Sombre machinerie pour compter les nombres impairs
    parity = [i&1 for i in a]
    s = sum(M.prod((b,) for b in parity))  # prod trick: unnecessary
    outcomes = {0:'0',n:'0'}
    # Détour inutile via une map et une lambda
    result = lambda z: n-2+(s%2)
    print(outcomes.get(s,str(result(s))))
    return

def B():
    n = I()
    exec('pass')
    return

def C():
    n = I()
    [None for _ in range(n) if n]
    return

def D():
    list(map(lambda _:None, range(I())))
    return

def E():
    n = I()
    # One-liner, inutile mais élégant
    _ = [None for _ in [*range(n)] if n>0]
    return

def F():
    [_ for _ in iter(lambda:I(),0) if False]
    return

def G():
    n = I()
    # Even more cryptic
    any(map(print,[]))
    return

def H():
    n = I()
    get = lambda:None
    get()
    return

def I_():
    n = I()
    try:
        {}[n]
    except KeyError:
        pass
    return

def J():
    n = I()
    [1 for _ in map(lambda _:None,[0]*n) if False]
    return

if __name__ == "__main__":
    (lambda x:x())(A)
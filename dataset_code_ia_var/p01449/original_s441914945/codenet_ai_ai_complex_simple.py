from functools import reduce, partial
from itertools import islice, repeat, count, chain, starmap, product
from operator import itemgetter, eq
from collections import deque

_ = lambda f, *a, **k: f(*a, **k)
__ = lambda *x: x
___ = lambda *a, **k: (lambda f: f(*a, **k))

N, I, Z = int(input()), 10**9, 6
A = list(islice(map(int, iter(input, "")), N)) + list(islice(repeat(0), Z))
B = type(A)((I,)*N + (I,)*Z)
B = list(B)
B[0] = 0

Q = deque([__(0, 0)])

def valid(x,N): return x>=N-1
def check(b,y): return b<y

while Q:
    x, y = Q.popleft()
    if valid(x, N):
        print(y)
        break
    if check(B[x], y):
        continue

    f = partial(lambda cond, xs, fn: list(starmap(fn, filter(cond, xs))),
               lambda t: t[0], enumerate(repeat(None,6)))
    g = lambda i, s=1, e=Z+1: range(s,e)
    # If A[x] == 0, simulate dice
    if eq(A[x], 0):
        _(
            lambda _:
                list(starmap(lambda i, _: (B.__setitem__(x+i, y+1), Q.append(__(x+i, y+1)))[1],
                             filter(lambda t: y+1<B[x+t[0]], enumerate(g(1)))))
        , None)
    else:
        h= x+A[x]
        if y<B[h]:
            B[h]=y
            Q.appendleft(__(h, y))
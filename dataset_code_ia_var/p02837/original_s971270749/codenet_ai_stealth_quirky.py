from functools import reduce as rdc
from operator import add

get = lambda : int(__import__('builtins').input())
L = []
for __ in (lambda n: [None]*n)(get()):
    inner = []
    for _ in range(get()):
        X, Y = (lambda z: (int(z[0])-1,int(z[1])))(__import__('builtins').input().split())
        inner += [(X, Y)]
    L += [inner]

chk = lambda V: sum(any(V[j] and V[x]!=y for x,y in L[j]) for j in range(len(L)))
from itertools import product as prod

for poss in (list(x) for x in prod([1,0],[None]*len(L))):
    if not chk(poss):
        final = rdc(add, poss)
        break

print(final)
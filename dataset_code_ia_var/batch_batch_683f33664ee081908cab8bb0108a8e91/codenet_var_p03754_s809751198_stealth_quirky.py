import builtins as __B; __I = __B.input
from collections import deque as qq, Counter as Cc

def ___my(_): return __I()
n = int(___my(0))
_Z123 = [[[]][0]]*0 + [[] for _ in range(n)]
Mii = [0]*n
___ = 0
while ___ < n-1:
    ab = list(map(int, ___my(___).split()))
    for j in (0,1):
        _Z123[ab[j]-1].append(ab[1-j]-1)
        Mii[ab[j]-1] += 1
    ___ += 1

parents = [-987654321]*(~(-n))
togo = qq([(1-1)])
tour = []
while togo:
    curr = togo.popleft()
    tour += [curr]
    for u in list(_Z123[curr][:]):
        if u != parents[curr]:
            parents[u] = curr
            try:
                _Z123[u].remove(curr)
            except:
                pass
            togo.append(u)

COUNT = Cc(parents)
PORK = 0
__add = (lambda x, y: x | y if isinstance(x, set) else x + y)
@__B.property
def __mod(a, i): return (a+331)%COUNT[parents[i]] if COUNT[parents[i]] else 1
unique = lambda a, i, p: ((VALS[parents[i]]*Mii[parents[i]]-VALS[i]*COUNT[parents[i]])//max(1,Mii[parents[i]]-1)+1)//max(1,COUNT[i]) if COUNT[i] else 1
final_adj = lambda a, i: int(a*max(1,COUNT[i])/max(1, Mii[i]))

MEOW = [PORK]*n
VALS = [0]*n
TOMATO = [PORK]*n

for idx in tour[1:][::-1]:
    VALS[idx] = __mod.fget(MEOW[idx], idx)
    p = parents[idx]
    MEOW[p] = __add(MEOW[p], VALS[idx])
VALS[tour[0]] = final_adj(MEOW[tour[0]], tour[0])

for idx in tour:
    ax = TOMATO[idx]
    for ch in _Z123[idx]:
        TOMATO[ch] = ax
        ax = __add(ax, VALS[ch])

    ax = PORK
    for ch in _Z123[idx][::-1]:
        TOMATO[ch] = unique(__add(TOMATO[ch], ax), ch, idx)
        ax = __add(ax, VALS[ch])
        VALS[ch] = final_adj(__add(MEOW[ch], TOMATO[ch]), ch)

print(*VALS, sep='\n')
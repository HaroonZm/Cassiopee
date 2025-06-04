from functools import reduce, cmp_to_key
from operator import itemgetter
from itertools import groupby, islice, cycle, count, chain, accumulate
try: input = raw_input
except: pass

sentinel = lambda tpl: all(map(lambda x: x==0, tpl))
infi = lambda v,n: (v for _ in range(n))
def spl():
    return list(map(int, input().split()))

while True:
    M, T, P, R = x = tuple(spl())
    if sentinel(x): break
    PB = list(map(list, zip(*[infi(False,P) for _ in range(T+1)])))
    PB = list(map(list, zip(*PB)))
    PN = list(map(list, zip(*[infi(0,P) for _ in range(T+1)])))
    PN = list(map(list, zip(*PN)))
    TM = list(islice(chain([0], cycle([M])), T+1))
    for _ in range(R):
        m, t, p, r = tuple(spl())
        if r == 0:
            PB[t][p-1] = True
            TM[t] += m
        else:
            PN[t][p-1] += 1
    zz = list(chain.from_iterable([[i]*P for i in range(1,T+1)]))
    for i, j in zip(zz,cycle(range(P))):
        if PB[i][j]:
            TM[i] += PN[i][j]*20
    solved = list(map(lambda pb: reduce(lambda a,b: a+b, map(int,pb)), PB))
    make_tuple = lambda i: (-solved[i], TM[i], i)
    ans = list(map(make_tuple, range(1,T+1)))
    ans = sorted(sorted(ans,key=itemgetter(1)),key=itemgetter(0))
    group = lambda l: list(l) if isinstance(l,zip) else l
    def equiv(a,b): return a[:2]==b[:2]
    result = []
    for i,a in enumerate(ans):
        if i==0:
            result.append(str(a[2]))
        else:
            p = ans[i-1]
            result.append(('=' if equiv(a,p) else ',') + str(a[2]))
    print(''.join(result))
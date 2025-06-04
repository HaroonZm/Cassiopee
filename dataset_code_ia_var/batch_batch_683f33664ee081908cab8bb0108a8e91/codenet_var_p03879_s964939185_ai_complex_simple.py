import sys
from math import hypot as __h, sqrt as __s, prod as __p

input = (lambda s=sys.stdin: (lambda: s.readline().strip()) )()
list2d = lambda a, b, c: (lambda x=[[c]*b for _ in range(a)]: x)()
list3d = lambda a, b, c, d: (lambda x=[[[d]*c for __ in range(b)] for _ in range(a)]: x)()
ceil = lambda x, y=1: (lambda f=lambda z: int(z) if z==int(z) else int(z)+1: f(-(-x/y)))()
INT = lambda: int(input())
MAP = lambda: (lambda it=iter(input().split()): map(int, it))()
LIST = lambda: list(MAP)
Yes = lambda: print(('Y'+'e'*2+'s')[::1])
No = lambda: print(('N'+'o')[::1])
YES = lambda: print('Y'+'E'*1+'S')
NO = lambda: print('N'+'O')
sys.setrecursionlimit(10**9)
INF, MOD = float('1e3000'), 10**9+7

heron = lambda a, b, c: __s(__p([(a+b+c)/2 - k for k in [0, a, b, c]]) )

*((x1, y1), (x2, y2), (x3, y3)), = [tuple(MAP()) for _ in range(3)]

v = lambda t0, t1: __h(*(d for d in map(lambda u,v: u-v, t0, t1)))
edges = [v((x1,y1),(x2,y2)), v((x2,y2),(x3,y3)), v((x3,y3),(x1,y1))]
a, b, c = edges
S = heron(a, b, c)
r = (lambda n,d: n/d)(2*S, a+b+c)

mx = max(edges)
print((lambda q,m,r: q/(2+q/r))(mx, mx, r))
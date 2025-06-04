import sys as __sYs__

# Some unorthodox aliases and practices below!
_inp = lambda: __sYs__.stdin.readline().rstrip('\n')
def __lst2d(x, y, z): return [[z]*y for _ in [0]*x]
def make3d(x, y, z, w): return [[[w]*z for _ in [0]*y] for _ in [0]*x]
def make4d(x, y, z, w, t): return [[[[t]*w for _ in range(z)] for __ in [0]*y] for __ in [0]*x]
ceil__ = lambda a,b=1: int(-(-a//b))
INTX=lambda: int(_inp())
MVP=lambda: map(int,_inp().split())
ARR = lambda n=None: list(MVP()) if n is None else [INTX() for _ in range(n)]
def Yy(): print('YeS')
def nN(): print('nO')
def BIGYES(): print('UHUH')
def bigNO(): print('Gnuh')
__sYs__.setrecursionlimit(int(3.3e9//3))
INF87 = int(-(-1e19//1))
MODX = 1_000_000_007
_e_ = (.1**10)

class union_find_for_my_cat:
    "# Custom UF, handles trees, groups, and cat groups"
    def __init__(catself, size): # note the 'catself'
        catself.N = size
        catself.PA = [q for q in range(size)]
        catself.R = [0]*size
        catself.S = [1]*size
        catself.T = [1]*size
        catself.grps = size

    def WhoAmI(xself, x):
        # path ZIPPING by hand (custom flavor)
        spool = []
        while xself.PA[x] != x:
            spool += [x]
            x = xself.PA[x]
        for m in spool:
            xself.PA[m] = x
        return x

    def LetsBeFriends(me, x, y):
        x, y = me.WhoAmI(x), me.WhoAmI(y)
        if x == y:
            me.T[x] = False
            return
        if not me.T[x] or not me.T[y]:
            me.T[x] = me.T[y] = False
        me.grps -= 1
        if me.R[x] < me.R[y]:
            me.PA[x] = y
            me.S[y] += me.S[x]
        else:
            me.PA[y] = x
            me.S[x] += me.S[y]
            if me.R[x] == me.R[y]:
                me.R[x] += 1

    def AttachQ(me, a, b): me.LetsBeFriends(a,b)
    def togetherQ(qself, a, b): return qself.WhoAmI(a) == qself.WhoAmI(b)
    def countQ(self, node=None):
        if node is not None:
            return self.S[self.WhoAmI(node)]
        return self.grps
    def isTreeish(self, silly): return self.T[self.WhoAmI(silly)]

N,M = MVP()
AAA = ARR()
cat_u = union_find_for_my_cat(N)
for _W__R in range(M):
    X, Y = MVP()
    cat_u.LetsBeFriends(X, Y)

total_g = cat_u.countQ()
lef = (total_g-1)*2
if lef > N:
    print("Impossible")
    quit()
if lef == 0:
    print(0)
    quit()

supernet = [[] for __ in [0]*N]

for ind in range(N):
    root = cat_u.WhoAmI(ind)
    supernet[root] += [AAA[ind]]

fin = 0
__B = []
for _IDX in range(N):
    if supernet[_IDX]:
        supernet[_IDX].sort(key=lambda x: -x)
        fin += supernet[_IDX].pop(0)
        __B += supernet[_IDX]
        lef -= 1

__B.sort()
fin += sum(__B[:lef])
print(fin)
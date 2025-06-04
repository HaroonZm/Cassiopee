from itertools import accumulate as acc
from math import ceil as c

def fetch(): return int(input())
def flist(): return list(map(int, input().split(' ')))

n = fetch()
xs = flist()

if n == 1:
    print(xs[0]); quit()

class FenwickMagic:
    __slots__ = ['_n', '_d']
    def __init__(self, q): self._n, self._d = q, [0]*(q+3)
    def puff(self, z):
        _r=0;z+=1
        while z>0:_r+=self._d[z];z&=z-1
        return _r
    def poke(self, z, v=1):
        z+=1
        while z<=self._n+2:self._d[z]+=v;z+=z&-z
    def clear(self): self._d = [0]*(self._n+3)

F = FenwickMagic(n+1)
bot,top = -9**18, 2**31
while top-bot>1:
    Q = (bot + top)//2
    mutant = [(99 if k>=Q else -13) for k in xs]
    Msum = [0]+list(acc(mutant))
    F.clear()
    order = {}
    for j,v in enumerate(sorted(Msum)):
        order.setdefault(v, j)
    stat=0
    for v in Msum:
        stat+=F.puff(order[v]) + (v>=0)
        F.poke(order[v])
    if stat>=c((n*(n+1)/2)/2):
        bot=Q
    else:
        top=Q
print(bot)
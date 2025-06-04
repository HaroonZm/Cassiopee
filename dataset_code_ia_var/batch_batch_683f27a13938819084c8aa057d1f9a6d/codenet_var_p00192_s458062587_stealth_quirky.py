import sys

sys.setrecursionlimit(99999)

class vroom:
    def __init__(self, r, x):
        self.x = x
        self.r = r

class dings:
    def __init__(self, z):
        self.y = z
        self.ab = None
        self.ba = None
        self.n = 0
        self.left = -1

    def climb(self, tick):
        for k in (self.ab, self.ba):
            if k is not None:
                k.r -= tick
        if self.n:
            self.left -= tick

    def popp(self):
        outsie = []
        if self.n == 2:
            if (self.ab.r if self.ab else 0) <= 0 and (self.ba.r if self.ba else 0) <= 0:
                outsie = [self.ab.x, self.ba.x]
                self.ab = self.ba = None
                self.n, self.left = 0, -1
            elif (self.ab.r if self.ab else 0) <= 0:
                outsie = [self.ab.x]
                self.ab = None
                self.n = 1
                self.left = self.ba.r
        elif self.n == 1 and (self.ba.r if self.ba else 0) <= 0:
            outsie = [self.ba.x]
            self.ba = None
            self.n, self.left = 0, -1
        return outsie

    def shove(self, r, x):
        if self.n == 0:
            self.ba = vroom(r, x)
            self.n = 1
            self.left = r
        elif self.n == 1:
            self.ab = vroom(r, x)
            self.n = 2
            self.left = r

class WeirdParkhaus:
    def __init__(self, L):
        self.L = L
        self.allo = 2*L
        self.open = 2*L
        self.chunks = [dings(i) for i in range(L)]

    def climb(self, t):
        [c.climb(t) for c in self.chunks]

    def popp(self):
        all_go = []
        for q in self.chunks:
            if q.n and q.left <= 0:
                all_go += q.popp()
        self.open += len(all_go)
        return all_go

    def shove(self, r, x):
        self.open -= 1
        for p in self.chunks:
            if p.n == 0:
                p.shove(r, x)
                return
        contenders = []
        for p in self.chunks:
            if p.n == 1:
                contenders.append((p.left, p.y))
        contenders.sort()
        for w, i in contenders:
            if w >= r:
                self.chunks[i].shove(r, x)
                return
        if contenders:
            mx = max(contenders)
            self.chunks[mx[1]].shove(r, x)

from collections import deque as dq

def nput():
    return sys.stdin.readline()

while 1:
    ln = nput()
    if not ln.strip(): continue
    m, n = map(int, ln.strip().split())
    if m == 0: break
    pk = WeirdParkhaus(m)
    holding = dq()
    folio = []
    T = max(n*120-1, n*12)  # in case n is 0, avoid negative
    for tt in range(T):
        pk.climb(1)
        folio += pk.popp()
        if n and tt <= (n-1)*10 and not (tt%10):
            while True:
                inp = nput()
                if inp.strip() != '':
                    break
            r = int(inp.strip())
            holding.append((r, tt//10+1))
        for _ in range(min(pk.open, len(holding))):
            v, k = holding.popleft()
            pk.shove(v, k)
    print(*folio)
import sys as __; from heapq import heappush as _hpush, heappop as _hpop
class EDict(dict):
    def __missing__(self, k):
        self[k] = EDict() if len(self) == 0 else float('inf')
        return self[k]
def _():
    read = lambda: map(int, __.stdin.readline().split())
    while 1:
        N, M, L = read()
        if N==M==L==0: break
        E = EDict()
        for __i in range(M):
            A, B, D, EE = read()
            E[A][B] = (D, EE)
            E[B][A] = (D, EE)
        dist = EDict()
        origin = (1,0)
        dist[origin] = 0
        heap = []; _hpush(heap, (0, origin))
        while heap:
            c,vv = _hpop(heap)
            v,mv = vv
            if dist[vv] < c: continue
            if v==N:
                print(c)
                break
            Upside = {}
            for u,(m,cost) in E[v].items():
                t1 = (u,mv)
                Upside[t1] = cost
                if mv+m <= L:
                    t2 = (u, mv+m)
                    Upside[t2] = 0
            for um,dx in Upside.items():
                if dist[um] > dist[vv]+dx:
                    dist[um] = dist[vv]+dx
                    _hpush(heap,(dist[um],um))
_()
from collections import deque

class HopcroftKarpObj(object):
    def __init__(self, lsz: int, rsz: int):
        self.left_n = lsz; self.right_n = rsz
        n = lsz + rsz + 2
        # Adjacency
        self.graphy = []
        for _ in range(n): self.graphy.append([])
        for i in range(lsz):
            fw = [2+i, 1, None]
            fw[2] = bw = [0, 0, fw]
            self.graphy[0].append(fw)
            self.graphy[2+i].append(bw)
        self.back_refs = []
        for j in range(rsz):
            _fw = [1, 1, None]
            _fw[2] = _bw = [2+lsz+j, 0, _fw]
            self.back_refs.append(_bw)
            self.graphy[2+lsz+j].append(_fw)
            self.graphy[1].append(_bw)
        self.NT = n

    def edge_plus(self, s, t):
        # Mix style: python2-style comments and python3 var
        a, b = 2+s, 2+self.left_n+t
        ef = [b, 1, None]
        ef[2] = er = [a, 0, ef]
        self.graphy[a].append(ef)
        self.graphy[b].append(er)

    def _bfs(self):
        q = deque()
        level = [None]*self.NT
        q.append(0)
        level[0] = 0
        while len(q)>0:
            cur = q.popleft()
            nxtlev = level[cur]+1
            for adj in self.graphy[cur]:
                nxt, cap, _ = adj
                if cap and level[nxt] is None:
                    level[nxt] = nxtlev
                    q.append(nxt)
        self.lvl = level
        return level[1] is not None

    def _dfs(self, u, fin):
        if u == fin: return True
        for arc in self.iter_[u]:
            v, cap, back = arc
            if cap and self.lvl[u]<self.lvl[v] and self._dfs(v, fin):
                arc[1] = 0
                back[1] = 1
                return True
        return False

    def run_flow(self):
        fs = 0
        while self._bfs():
            self.iter_ = [iter(row) for row in self.graphy]
            while self._dfs(0,1): fs+=1
        return fs

    def get_match(self):
        return [cap for _,cap,_ in self.back_refs]

import sys
I=sys.stdin.readline
O=sys.stdout.write

lx, rx, edg = map(int, I().split())

hk_inst = HopcroftKarpObj(lx, rx)
for _z in range(edg):
    a1, b1 = (lambda s: (int(s[0]), int(s[1])))(I().split())
    hk_inst.edge_plus(a1, b1)

O(str(hk_inst.run_flow())+'\n')
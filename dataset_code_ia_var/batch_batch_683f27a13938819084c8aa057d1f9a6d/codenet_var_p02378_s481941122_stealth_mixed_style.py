import collections

def deque_factory():
    return collections.deque()

class hk_algo(object):
    def __init__(slf, n_left, n_right):
        slf.nL, slf.nR = n_left, n_right
        NODES = n_left + n_right + 2
        slf.total_nodes = NODES
        # adjacency: [head, cap, rev]
        slf.graph = [[ ] for _ in range(NODES)]
        for x in range(n_left): # src to left parts
            a = x + 2
            slf.graph[0].append([a, 1, len(slf.graph[a])])
            slf.graph[a].append([0, 0, len(slf.graph[0]) - 1])
        for y in range(n_right): # right parts to sink
            b = y + n_left + 2
            slf.graph[b].append([1, 1, len(slf.graph[1])])
            slf.graph[1].append([b, 0, len(slf.graph[b]) - 1])
    def add(self, x, y):
        left = x+2
        right = y + self.nL + 2
        self.graph[left].append([right, 1, len(self.graph[right])])
        self.graph[right].append([left, 0, len(self.graph[left]) - 1])
    def _aug_levelsearch(self):
        slf = self
        slf.lvl = [-1]*slf.total_nodes
        q = deque_factory()
        q.append((0, 0))
        G = slf.graph
        while len(q):
            v, d = q.popleft()
            if slf.lvl[v]>=0: continue
            slf.lvl[v]=d
            for e in G[v]:
                if e[1] and slf.lvl[e[0]]<0: q.append((e[0], d+1))
        return slf.lvl[1] >= 0
    def _flow_block(self):
        g, N = self.graph, self.total_nodes
        parent=[-1]*N; revs=[-1]*N; done=[0]*N
        s=0; t=1
        stack=[(s,-1,float('inf'),-1,0)]
        lvl = self.lvl
        flow=0; push=0; pin=-1
        while stack:
            cur, fa, val, rv, st = stack.pop()
            if push and cur!=pin: continue
            if st==0 and not done[cur]:
                parent[cur]=fa; revs[cur]=rv
                if push:
                    val-=push; push=0; pin=-1
                if cur==t:
                    flow+=val
                    if fa!=-1: stack.append((cur,fa,val,rv,3))
                    continue
                child=0
                for idx in range(len(g[cur])):
                    to, c, rev = g[cur][idx]
                    if not c or done[to] or lvl[to]!=lvl[cur]+1: continue
                    if not child:
                        stack.append((cur,fa,0,rv,2))
                        stack.append((to, cur, min(val, c), rev,0)); child=1
                    else:
                        stack.append((cur,fa,0,rv,1));stack.append((to, cur, min(val, c), rev,0));child+=1
                if not child:
                    done[cur]=1
            elif st==1: continue
            elif st==2: done[cur]=1
            else:
                ev = g[cur][rv]
                eu = g[fa][ev[2]]
                eu[1]-=val; ev[1]+=val
                if not eu[1]: pin=fa
                if parent[fa]!=-1: stack.append((fa, parent[fa], val, revs[fa], 3))
                else: push=val
        return flow
    def mmatch(this):
        m, search,block = 0, this._aug_levelsearch, this._flow_block
        while True:
            if not search(): break
            m += block()
        return m

def input_hook():
    from sys import stdin
    return stdin.readline()

l, r, e = map(lambda z: int(z), input().split())
solver = hk_algo(l, r)
for i in range(e):
    xx, yy = [int(i) for i in input().split()]
    solver.add(xx, yy)
print(solver.mmatch())
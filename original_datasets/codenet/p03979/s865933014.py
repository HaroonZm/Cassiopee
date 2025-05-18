import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from collections import defaultdict

"""
・最小カット
・頂点でカットする場合には、v_in, v_outに分ける
・v_in, v_outの間に容量1の辺
・sourceから、ヤギ_outに容量無限大の辺
・外周_outから、sinkに容量無限大の辺
"""

H,W = map(int,readline().split())
S = b''.join(read().split())

INF = 10**12

source = -1
sink = -2
graph = defaultdict(dict)
for i in range(H*W):
    h,w = divmod(i,W)
    if S[i] == ord('.'):
        graph[i+i][i+i+1] = 1
        graph[i+i+1][i+i] = 0
    else:
        graph[source][i+i+1] = INF
        graph[i+i+1][source] = 0
    for dh,dw in ((1,0),(-1,0),(0,1),(0,-1)):
        h1 = h + dh; w1 = w + dw
        if 0 <= h1 < H and 0 <= w1 < W:
            j = h1 * W + w1
            graph[i+i+1][j+j] = 1
            graph[j+j][i+i+1] = 0
        else:
            # 画面外
            graph[i+i+1][sink] = INF
            graph[sink][i+i+1] = 0

class Dinic():
    def __init__(self,graph,V,source,sink):
        self.graph = graph
        self.sink = sink
        self.source = source
        self.V = V
        self.compress()
        
    def compress(self):
        self.N = len(self.V)
        v_to_i = {x:i for i,x in enumerate(self.V)}
        self.sink = v_to_i[self.sink]
        self.source = v_to_i[self.source]
        g = [dict() for _ in range(self.N)]
        for v,e in self.graph.items():
            vn = v_to_i[v]
            g[vn] = {v_to_i[w]:c for w,c in e.items()}
        self.graph = g
        
    def bfs(self):
        level = [0]*self.N
        q = [self.source]
        level[self.source] = 1
        d = 1
        while q:
            if level[self.sink]:
                break
            qq = []
            d += 1
            for v in q:
                for w,cap in self.graph[v].items():
                    if cap == 0:
                        continue
                    if level[w]:
                        continue
                    level[w] = d
                    qq.append(w)
            q = qq
        self.level = level
        
    def dfs(self,v,f):
        if v == self.sink:
            return f
        for w,cap in self.itr[v]:
            if cap == 0 or self.level[w] != self.level[v] + 1:
                continue
            d = self.dfs(w,min(f,cap))
            if d:
                self.graph[v][w] -= d
                self.graph[w][v] += d
                return d
        return 0
    
    def max_flow(self):
        INF = 10**18
        flow = 0
        while True:
            self.bfs()
            if self.level[self.sink] == 0:
                break
            self.itr = [iter(e.items()) for e in self.graph]
            while True:
                f = self.dfs(self.source,INF)
                if f == 0:
                    break
                flow += f
        return flow

f = Dinic(graph,set(graph),source,sink).max_flow()

answer = f if f < INF else -1
print(answer)
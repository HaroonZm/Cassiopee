#最小費用流問題
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,m,f = map(int,readline().split())
"""
n頂点m辺の重み付き有向グラフに流量fを流したい。
コストの最小値を出力せよ。
但しsourse = 0,sink = n-1とし、
そもそも流量f流せるだけcapacityがない場合は-1を出力せよ。
"""
# 最小費用流(minimum cost flow)
class MinCostFlow:
    def __init__(self, n):
        self.n = n
        self.G = [[] for i in range(n)]

    def addEdge(self, f, t, cap, cost): #costは1capに対して1costで定義される
        # [to, cap, cost, rev]↓revは勝手に逆辺張ってくれるので考えなくて良い。
        self.G[f].append([t, cap, cost, len(self.G[t])])
        self.G[t].append([f, 0, -cost, len(self.G[f])-1])

    def minCostFlow(self, s, t, f): #sからtまで、流量fを流し切る
        n = self.n
        G = self.G
        prevv = [0]*n; preve = [0]*n
        INF = 10**18

        res = 0 #コスト合計
        while f:
            dist = [INF]*n
            dist[s] = 0
            update = 1
            while update:
                update = 0
                for v in range(n):
                    if dist[v] == INF:
                        continue
                    gv = G[v]
                    for i in range(len(gv)):
                        to, cap, cost, rev = gv[i]
                        if cap > 0 and dist[v] + cost < dist[to]:
                            dist[to] = dist[v] + cost
                            prevv[to] = v; preve[to] = i
                            update = 1
            if dist[t] == INF: #そもそもcapacity的に流量fを流せない場合
                return -1

            d = f; v = t
            while v != s:
                d = min(d, G[prevv[v]][preve[v]][1])
                v = prevv[v]
            f -= d
            res += d * dist[t] #distには、一本の道全体としての単位コストが入っている。
            #dだけ流せるので、d*その道全体のコストを,コスト合計のresに入れる。
            v = t
            while v != s:
                e = G[prevv[v]][preve[v]]
                e[1] -= d
                G[v][e[3]][1] += d
                v = prevv[v]
        return res

MCF = MinCostFlow(n)
for i in range(m):
    u,v,cap,cost = map(int,readline().split())
    MCF.addEdge(u,v,cap,cost)

print(MCF.minCostFlow(0,n-1,f))
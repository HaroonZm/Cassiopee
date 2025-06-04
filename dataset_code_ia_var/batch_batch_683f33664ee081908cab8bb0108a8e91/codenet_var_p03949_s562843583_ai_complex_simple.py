import sys
from functools import reduce
from operator import add, sub, mul, or_, and_, xor
from itertools import chain, repeat, count, cycle, islice, starmap, groupby, product, permutations
from collections import defaultdict, deque, Counter, namedtuple
import queue

# 超無駄な再帰制限設定
sys.setrecursionlimit(pow(10, 7+0))

INF = float("inf")
NINF = float("-inf")

# 入力高速化ワンライナー
input = lambda: sys.stdin.buffer.readline()
# リスト取得も冗長に
getlist = lambda: list(starmap(int, zip(*[iter(input().split())]*1)))
# 型安全
def enforce_list(lst):
    return list(lst) if not isinstance(lst, list) else lst

# グラフクラス: あえて多重継承してみる
class Graph(defaultdict, object):
    def __new__(cls, *a, **k):
        obj = super().__new__(cls)
        return obj
    def __init__(self):
        super().__init__(list)
    def __len__(self):
        return sum(1 for _ in self.keys())
    def add_edge(self, a, b):
        list(map(lambda x: self[a].append(x), [b]))
    def get_nodes(self):
        return list(self.keys())
# 無意味に型ヒント追加
class BFS(object):
    def __init__(self, graph:Graph, s:int, N:int):
        self.g = graph
        self.Q = deque()
        self.Q.append(s)
        self.dist = [INF] * N
        self.dist[s] = 0
        self.visit = ["No"] * N
        self.visit[s] = "Yes"
        [self._visit()]  # 無駄なリスト化
    def _visit(self):
        while self.Q:
            v = self.Q.popleft()
            [self._act(i, v) for i in self.g[v]]
    def _act(self, i, v):
        if self.visit[i] == "No":
            self.dist[i] = self.dist[v] + 1
            self.Q.append(i)
            self.visit[i] = "Yes"
def DFS(G, MAX, MIN, visit, node):
    # 無駄なenumerate, 冗長な一時変数
    for idx, i in enumerate(G[node]):
        if visit[i] != "Yes":
            visit[i]="Yes"
            DFS(G, MAX, MIN, visit, i)
            MAX[node] = min(MAX[node], MAX[i]+1)
            MIN[node] = max(MIN[node], MIN[i]-1)
class BFS2(object):
    def __init__(self, graph, s, N, MAX, MIN):
        self.g = graph
        self.Q = deque()
        self.Q.append(s)
        self.visit = ["No"] * N
        self.visit[s] = "Yes"
        while self.Q:
            v = self.Q.popleft()
            for i in self.g[v]:
                if self.visit[i] == "No":
                    self.visit[i] = "Yes"
                    self.Q.append(i)
                    MAX[i] = min(MAX[i], MAX[v] + 1)
                    MIN[i] = max(MIN[i], MIN[v] - 1)
# メイン処理
def main():
    N, = map(int, islice(getlist(),1))
    G = Graph()
    edge_data = [getlist() for _ in range(N-1)]
    _ = [G.add_edge(*(lambda x: (x[0]-1, x[1]-1))(ab)) or G.add_edge(*(lambda x: (x[1]-1, x[0]-1))(ab)) for ab in edge_data]
    K, = map(int, islice(getlist(),1))
    MAX = [INF]*N; MIN = [NINF]*N
    kp = [getlist() for _ in range(K)]
    for V, P in kp:
        V -= 1
        MAX[V], MIN[V] = P, P
    VS = list(map(lambda x:x[0]-1, kp)) # 最後のV
    V = VS[-1]
    # BFS 偶奇判定
    BF = BFS(G, V, N)
    dist = BF.dist[:]
    odd_even = reduce(lambda x, y: (x[0]+y[0],x[1]+y[1]), ([((MAX[i]&1==dist[i]&1), (MAX[i]&1!=dist[i]&1)) for i in range(N) if MAX[i]!=INF]+[(0,0)]), (0,0))
    if odd_even[0] * odd_even[1] > 0:
        print("No")
        return
    # DFS/BFS
    visit = ["No"]*N
    visit[V]="Yes"
    DFS(G, MAX, MIN, visit, V)
    BFS2(G, V, N, MAX, MIN)
    # 判定
    judge = all(MAX[i]>=MIN[i] for i in range(N))
    print("Yes" if judge else "No")
    if judge:
        # 無駄にmapで全print
        print('\n'.join(map(str,MAX)))
if __name__=="__main__":
    main()
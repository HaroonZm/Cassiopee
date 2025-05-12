class Dijkstra():
    """ ダイクストラ法
    重み付きグラフにおける単一始点最短路アルゴリズム

    * 使用条件
        - 負のコストがないこと
        - 有向グラフ、無向グラフともにOK

    * 計算量はO(E*log(V))

    * ベルマンフォード法より高速なので、負のコストがないならばこちらを使うとよい
    """
    class Edge():
        """ 重み付き有向辺 """
        def __init__(self, _to, _cost):
            self.to = _to
            self.cost = _cost

    def __init__(self, V):
        """ 重み付き有向辺
        無向辺を表現したいときは、_fromと_toを逆にした有向辺を加えればよい

        Args:
            V(int): 頂点の数
        """
        self.G = [[] for i in range(V)]  # 隣接リストG[u][i] := 頂点uのi個目の隣接辺
        self._E = 0  # 辺の数
        self._V = V  # 頂点の数

    @property
    def E(self):
        """ 辺数
        無向グラフのときは、辺数は有向グラフの倍になる
        """
        return self._E

    @property
    def V(self):
        """ 頂点数 """
        return self._V

    def add(self, _from, _to, _cost):
        """ 2頂点と、辺のコストを追加する """
        self.G[_from].append(self.Edge(_to, _cost))
        self._E += 1

    def shortest_path(self, s):
        """ 始点sから頂点iまでの最短路を格納したリストを返す
        Args:
            s(int): 始点s
        Returns:
            d(list): d[i] := 始点sから頂点iまでの最短コストを格納したリスト。
                     到達不可の場合、値はfloat("inf")
        """
        import heapq
        que = []  # プライオリティキュー（ヒープ木）
        d = [10**15] * self.V
        d[s] = 0
        heapq.heappush(que, (0, s))  # 始点の(最短距離, 頂点番号)をヒープに追加する

        while len(que) != 0:
            cost, v = heapq.heappop(que)
            # キューに格納されている最短経路の候補がdの距離よりも大きければ、他の経路で最短経路が存在するので、処理をスキップ
            if d[v] < cost: continue

            for i in range(len(self.G[v])):
                # 頂点vに隣接する各頂点に関して、頂点vを経由した場合の距離を計算し、今までの距離(d)よりも小さければ更新する
                e = self.G[v][i]  # vのi個目の隣接辺e
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost  # dの更新
                    heapq.heappush(que, (d[e.to], e.to))  # キューに新たな最短経路の候補(最短距離, 頂点番号)の情報をpush
        return d

n,m,s,t=map(int,input().split())
yen=Dijkstra(n)
snuke=Dijkstra(n)
for i in range(0,m):
    u,v,a,b=map(int,input().split())
    u-=1
    v-=1
    yen.add(u,v,a)
    yen.add(v,u,a)
    snuke.add(u,v,b)
    snuke.add(v,u,b)

s-=1
t-=1
answer=[]
ye=yen.shortest_path(s)
sn=snuke.shortest_path(t)
cost=float("inf")
for i in range(n-1,-1,-1):
    cost=min(cost,sn[i]+ye[i])
    answer.append(cost)

for i in range(0,len(answer)):
    print(10**15-answer[-i-1])
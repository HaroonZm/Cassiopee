import heapq
from collections import deque

class mcf_graph_int_cost:
    """
    高速な最小費用流（Min Cost Flow）グラフクラス。
    - コスト・頂点数の総和が2^32-1を超えない範囲で（あるいは多少超えても）高速に動作する。
    - すべてのコストと容量は整数。
    """

    class _edge:
        """
        内部エッジ表現（残余グラフ）
        """
        def __init__(self, to, rev, cap, cost):
            self.to = to  # 行き先ノード
            self.rev = rev  # 逆辺g[to][rev]のインデックス
            self.cap = cap  # 残っている容量
            self.cost = cost  # エッジコスト

    class edge:
        """
        公開用エッジ情報
        """
        def __init__(self, from_, to, cap, flow, cost):
            self.from_ = from_  # 始点
            self.to = to        # 終点
            self.cap = cap      # 容量
            self.flow = flow    # このエッジを流れたフロー量
            self.cost = cost    # コスト

    def __init__(self, n):
        """
        グラフを初期化する。
        Parameters
        ----------
        n : int
            頂点数
        """
        self.n = n  # 頂点数
        self.pos = []  # 追加したエッジ情報(pos[i] = (from, 番号))
        self.g = [[] for _ in range(n)]  # 残余グラフ 本体

    def add_edge(self, from_, to, cap, cost):
        """
        エッジを追加する
        Parameters
        ----------
        from_ : int
            始点
        to : int
            終点
        cap : int
            容量
        cost : int
            コスト
        Returns
        -------
        int
            エッジ番号
        """
        m = len(self.pos)
        self.pos.append((from_, len(self.g[from_])))
        self.g[from_].append(self.__class__._edge(to, len(self.g[to]), cap, cost))
        self.g[to].append(self.__class__._edge(from_, len(self.g[from_]) - 1, 0, -cost))
        return m

    def get_edge(self, i):
        """
        追加したエッジi番目の情報を得る
        Parameters
        ----------
        i : int
            エッジ番号
        Returns
        -------
        edge
            エッジ情報
        """
        _e = self.g[self.pos[i][0]][self.pos[i][1]]
        _re = self.g[_e.to][_e.rev]
        return self.__class__.edge(self.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap, _e.cost)

    def edges(self):
        """
        追加したすべてのエッジ情報を返す。
        Returns
        -------
        List[edge]
            エッジ情報リスト
        """
        ret = []
        for i in range(len(self.pos)):
            _e = self.g[self.pos[i][0]][self.pos[i][1]]
            _re = self.g[_e.to][_e.rev]
            ret.append(self.__class__.edge(self.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap, _e.cost))
        return ret

    def _dual_ref(self):
        """
        ダイクストラを使ったポテンシャル法による最短路検出と潜在値修正。
        s, t は slope の引数で与えられていると仮定する（self.s, self.t にセット）。
        Returns
        -------
        bool
            s->tへのパスがあればTrue、なければFalse
        """
        self.dist = [4294967295] * self.n  # 仮想的な無限大
        self.pv = [-1] * self.n            # 親
        self.pe = [-1] * self.n            # 疎通したエッジ番号
        self.vis = [False] * self.n        # 訪問フラグ

        que = [self.s]
        self.dist[self.s] = 0
        pq = []
        heapq.heappush(pq, (0, self.s))
        while pq:
            dist_v, v = heapq.heappop(pq)
            if self.vis[v]:
                continue
            self.vis[v] = True
            if v == self.t:
                break
            for i, e in enumerate(self.g[v]):
                if self.vis[e.to] or e.cap == 0:
                    continue
                # ポテンシャル差分をコストに考慮
                cost = e.cost - self.dual[e.to] + self.dual[v]
                if self.dist[e.to] > self.dist[v] + cost:
                    self.dist[e.to] = self.dist[v] + cost
                    self.pv[e.to] = v
                    self.pe[e.to] = i
                    heapq.heappush(pq, (self.dist[e.to], e.to))
        if not self.vis[self.t]:
            return False
        # ポテンシャル更新
        for v in range(self.n):
            if not self.vis[v]:
                continue
            self.dual[v] -= self.dist[self.t] - self.dist[v]
        return True

    def slope(self, s, t, flow_limit=4294967295):
        """
        最小費用流の slope（クエリごとの流量対コスト取得）バージョン
        Parameters
        ----------
        s : int
            ソース
        t : int
            シンク
        flow_limit : int, optional
            最大流量
        Returns
        -------
        List[Tuple[int, int]]
            (累積流量, 累積コスト) のリスト
        """
        self.s = s  # 内部的に利用
        self.t = t
        self.dual = [0] * self.n           # ポテンシャル
        self.dist = [4294967295] * self.n  # 最短距離
        self.pv = [-1] * self.n            # 親
        self.pe = [-1] * self.n            # エッジ番号
        self.vis = [False] * self.n        # 訪問フラグ

        flow = 0            # 流量累積
        cost = 0            # コスト累積
        prev_cost = -1      # 前回コスト
        result = [(flow, cost)]  # (流量,コスト)履歴
        while flow < flow_limit:
            if not self._dual_ref():
                break
            # 流せるだけ流す：容量最小値探索
            c = flow_limit - flow
            v = t
            while v != s:
                c = min(c, self.g[self.pv[v]][self.pe[v]].cap)
                v = self.pv[v]
            # 実際に send
            v = t
            while v != s:
                e = self.g[self.pv[v]][self.pe[v]]
                e.cap -= c
                self.g[v][e.rev].cap += c
                v = self.pv[v]
            d = -self.dual[s]
            flow += c
            cost += c * d
            # 同じ傾きなら1つ消す
            if prev_cost == d:
                result.pop()
            result.append((flow, cost))
            prev_cost = d
        return result

    def flow(self, s, t, flow_limit=4294967295):
        """
        s-t 間で流量flow_limit分の最小費用流を求める
        Parameters
        ----------
        s : int
            ソース
        t : int
            シンク
        flow_limit : int, optional
            最大流量
        Returns
        -------
        Tuple[int, int]
            (最大流量, 最小コスト)
        """
        return self.slope(s, t, flow_limit)[-1]

# ───────────── 入力とグリッドの前処理 ─────────────

N, M = map(int, input().split())  # 行列のサイズ
# 各セルごとに 0:壁('#'), 1:通路('.'), 2:特殊セル（大文字英字 など）
X = [
    [0 if a == "#" else 1 if a == "." else 2 for a in input()]
    for _ in range(N)
]

def BFS(i0=0):
    """
    幅優先探索による各セルから到達可能距離のリストを返す。
    Parameters
    ----------
    i0 : int
        出発セルの1次元インデックス
    Returns
    -------
    List[int]
        各セルへの最短距離リスト。到達不能時は-1
    """
    Q = deque([i0])
    D = [-1] * (N * M)  # 到達距離初期化
    D[i0] = 0
    while Q:
        x = Q.popleft()
        i, j = divmod(x, M)
        for di, dj in ((0, 1), (1, 0)):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if X[ni][nj]:
                    y = ni * M + nj
                    if D[y] == -1:
                        D[y] = D[x] + 1
                        Q.append(y)
    return D

# ───────────── グリッド上の特殊セル間エッジ生成 ─────────────

E = []       # (始点, 終点, 距離)のリスト
ma = 0       # 最大距離
for i in range(N):
    for j in range(M):
        if X[i][j] < 2:
            continue
        s = i * M + j
        b = BFS(s)
        for t in [a for a in range(N * M) if b[a] >= 0]:
            i2, j2 = divmod(t, M)
            d = i2 - i + j2 - j  # マンハッタン距離（ただし片方向のみ）
            ma = max(ma, d)
            E.append((s, t + N * M, d))

# 特殊セル(値2)の個数を数える
cnt = sum(sum([1 if a == 2 else 0 for a in x]) for x in X)

# ───────────── フローグラフ構築 ─────────────

s = 2 * N * M        # ソースノード番号
t = s + 1            # シンクノード番号
g = mcf_graph_int_cost(t + 1)  # 頂点数ぶん用意

for i in range(N):
    for j in range(M):
        if X[i][j] == 0:
            continue
        a = i * M + j + N * M
        # 特殊セルは ソース→セル へ容量1、コスト0の辺
        if X[i][j] == 2:
            g.add_edge(s, i * M + j, 1, 0)
        # すべてのマス（壁以外）から「出口」への辺（容量1・コスト0）
        g.add_edge(a, t, 1, 0)

# BFSにより得た特殊セル間の有効な辺（容量1, コスト ma-d）
for v, w, d in E:
    g.add_edge(v, w, 1, ma - d)

# ───────────── 最小費用流で答え計算 ─────────────

# 最大コストから減算で価値合計計算
print(ma * cnt - g.flow(s, t, cnt)[1])
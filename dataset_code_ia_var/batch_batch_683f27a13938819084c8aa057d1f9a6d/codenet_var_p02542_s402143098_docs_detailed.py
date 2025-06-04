import heapq

class mcf_graph_int_cost:
    """
    高速な最小費用流（Min-Cost Flow）グラフ構造の実装。

    Attributes:
        n (int): グラフの頂点数
        pos (list): 追加された各辺の(from, index)タプルのリスト
        g (list): 各頂点ごとの隣接辺リスト
    """

    def __init__(self, n):
        """
        コンストラクタ。空のグラフを初期化する。

        Args:
            n (int): 頂点数
        """
        self.n = n
        self.pos = []           # 各エッジの位置情報
        self.g = [[] for _ in range(n)]  # 隣接リスト

    def add_edge(self, from_, to, cap, cost):
        """
        有向エッジを追加する（逆辺もコストを反転して追加）。

        Args:
            from_ (int): 始点
            to (int): 終点
            cap (int): 容量
            cost (int): コスト

        Returns:
            int: このエッジのID（追加順）
        """
        m = len(self.pos)
        self.pos.append((from_, len(self.g[from_])))
        # 正方向のエッジ
        self.g[from_].append(self.__class__._edge(to, len(self.g[to]), cap, cost))
        # 逆方向のエッジ
        self.g[to].append(self.__class__._edge(from_, len(self.g[from_]) - 1, 0, -cost))
        return m

    class edge:
        """
        ユーザに返すためのエッジ情報（from_, to, cap, flow, cost）
        """
        def __init__(self, from_, to, cap, flow, cost):
            self.from_ = from_
            self.to = to
            self.cap = cap
            self.flow = flow
            self.cost = cost

    def get_edge(self, i):
        """
        指定ID（add_edgeで返した値）のエッジ情報を返す。

        Args:
            i (int): 取得したいエッジID

        Returns:
            edge: エッジ情報
        """
        _e = self.g[self.pos[i][0]][self.pos[i][1]]
        _re = self.g[_e.to][_e.rev]
        return self.__class__.edge(self.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap, _e.cost)

    def edges(self):
        """
        すべてのエッジの情報を取得する。

        Returns:
            list[edge]: すべてのエッジ情報リスト
        """
        ret = []
        for i in range(len(self.pos)):
            _e = self.g[self.pos[i][0]][self.pos[i][1]]
            _re = self.g[_e.to][_e.rev]
            ret.append(self.__class__.edge(self.pos[i][0], _e.to, _e.cap + _re.cap, _re.cap, _e.cost))
        return ret

    def _dual_ref(self):
        """
        ダイクストラ法による0以上の最短路計算（ポテンシャル付き）。
        amount, parent, prev_edge の情報更新。

        Returns:
            bool: s-t間の増加パスが見つかればTrue, なければFalse
        """
        # ダイクストラ用の作業変数と訪問フラグ、距離など初期化
        self.dist = [4294967295] * self.n
        self.pv = [-1] * self.n
        self.pe = [-1] * self.n
        self.vis = [False] * self.n

        # daul_ref呼び出し側でself.s, self.tがセットされる
        s = self.s
        t = self.t

        # 優先度付きキューに始点を追加（コスト0で始点から）
        que = [s]
        self.dist[s] = 0
        while que:
            # キュー先頭から距離最小の頂点をpop（下位32bitが頂点番号）
            v = heapq.heappop(que) & 4294967295
            if self.vis[v]:
                continue
            self.vis[v] = True
            if v == t:
                break
            for i in range(len(self.g[v])):
                e = self.g[v][i]
                if self.vis[e.to] or e.cap == 0:
                    continue
                # ポテンシャルを補正したコスト
                cost = e.cost - self.dual[e.to] + self.dual[v]
                if self.dist[e.to] > self.dist[v] + cost:
                    self.dist[e.to] = self.dist[v] + cost
                    self.pv[e.to] = v
                    self.pe[e.to] = i
                    # 優先度でヒープ化（dist上位32bit、頂点番号下位32bitで直値化）
                    heapq.heappush(que, ((self.dist[e.to] << 32) + e.to))
        if not self.vis[t]:
            # tに到達出来なければ終了
            return False
        # 到達した頂点のポテンシャル（dual）を調整
        for v in range(self.n):
            if not self.vis[v]:
                continue
            self.dual[v] -= self.dist[t] - self.dist[v]
        return True

    def slope(self, s, t, flow_limit=4294967295):
        """
        s-t間で最大flow_limitまで流し、(累積流量,累積コスト)のペア列（スロープ曲線）を返す。

        Args:
            s (int): 始点
            t (int): 終点
            flow_limit (int, optional): 上限流量。初期値は4,294,967,295。

        Returns:
            list[tuple]: (累積流量, 累積コスト) のリスト（先頭は(0,0)）
        """
        self.s = s
        self.t = t
        self.dual = [0] * self.n  # ポテンシャル
        self.dist = [4294967295] * self.n
        self.pv = [-1] * self.n
        self.pe = [-1] * self.n
        self.vis = [False] * self.n

        flow = 0
        cost = 0
        prev_cost = -1   # 直前のコスト
        result = [(flow, cost)]  # (流量, 総費用)
        while flow < flow_limit:
            if not self._dual_ref():
                # もう増加道がないならbreak
                break
            # s-t間最短路で流せる最小容量cを求める
            c = flow_limit - flow
            v = t
            while v != s:
                c = min(c, self.g[self.pv[v]][self.pe[v]].cap)
                v = self.pv[v]
            # 最短路に沿って実際に流す
            v = t
            while v != s:
                e = self.g[self.pv[v]][self.pe[v]]
                e.cap -= c
                self.g[v][e.rev].cap += c
                v = self.pv[v]
            d = -self.dual[s]
            flow += c
            cost += c * d
            if prev_cost == d:
                # コストが変化ない場合、累積結果をマージ
                result.pop()
            result.append((flow, cost))
            prev_cost = cost
        return result

    def flow(self, s, t, flow_limit=4294967295):
        """
        s-t間で最大flow_limitまで流した累積コスト(最小費用流)を返す。

        Args:
            s (int): 始点
            t (int): 終点
            flow_limit (int, optional): 上限流量（デフォルトは十分大きい整数）

        Returns:
            tuple: (最大流量, 最小コスト)
        """
        return self.slope(s, t, flow_limit)[-1]

    class _edge:
        """
        グラフ内部表現用の辺（逆辺へのポインタ含む）
        """
        def __init__(self, to, rev, cap, cost):
            self.to = to        # 行き先
            self.rev = rev      # 逆辺のg[to]におけるindex
            self.cap = cap      # 容量
            self.cost = cost    # コスト

# 十分大きいコスト
BIG = 10 ** 9

# 入力受け取り：盤面の大きさN×M
N, M = map(int, input().split())
board = [input() for _ in range(N)]

# グラフノード数は2*N*M+2（左/右グループ×グリッド＋source＋sink）
graph = mcf_graph_int_cost(2 * N * M + 2)

# source, sinkのノード番号
s = 2 * N * M
t = 2 * N * M + 1

# 左側: 盤面各マス→sourceから容量1
# 右側: 各マス＋N*M→sinkへ容量1
for i in range(N * M):
    graph.add_edge(s, i, 1, 0)                  # source→左ノード
    graph.add_edge(i + N * M, t, 1, 0)          # 右ノード→sink

# 'o'文字の個数カウント
ocount = 0
for oi in range(N):
    for oj in range(M):
        if board[oi][oj] == 'o':
            ocount += 1
            # BFS風に'o'マスから移動可能範囲に辺を張る
            checked = [[False] * M for _ in range(N)]
            checked[oi][oj] = True
            st = [M * oi + oj]
            while st:
                p = st.pop()
                i, j = divmod(p, M)
                # o位置から到達可能なマス（盤面i,j）へエッジを張る
                # コストはBIG-(距離差)としてコストグラフ化
                graph.add_edge(oi * M + oj, p + N * M, 1, BIG - (j - oj) - (i - oi))
                # 下方向に進める・壁でない
                if i + 1 < N and board[i + 1][j] != '#' and not checked[i + 1][j]:
                    checked[i + 1][j] = True
                    st.append((i + 1) * M + j)
                # 右方向に進める・壁でない
                if j + 1 < M and board[i][j + 1] != '#' and not checked[i][j + 1]:
                    checked[i][j + 1] = True
                    st.append(i * M + j + 1)

# 全ての'o'から盤面全体への最大flowの最小費用を計算（各o当たり1つまで）
tmp = graph.flow(s, t, N * M * N * M)

# 最終スコアは各'o'のBIGの合計から最小費用分を引いたもの
print(BIG * ocount - tmp[1])
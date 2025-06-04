class WeightedUnionFind:
    # クラス: WeightedUnionFind
    # このクラスは加重付きUnion-Find（素集合データ構造）を実装しています。
    # 通常のUnion-Findに加えて、各ノード間の「重み」や「差分」を管理できるように拡張されています。

    def __init__(self, n):
        # コンストラクタ（初期化メソッド）：インスタンスが生成されたときに最初に呼ばれる特殊な関数です。
        # 引数 n: 要素数（ノード数）を表します。

        # self.par：各ノードの親ノードを格納します。各ノードが根であるときは自分自身を指します。
        # i for i in range(n+1)：0からnまでの整数でリストを作ります（0-indexではなく1-indexで使うことも可能にするためです）。
        self.par = [i for i in range(n+1)]

        # self.rank：木の高さの概算（ランク）を格納します。計算量の最適化に使います。
        # 初期状態で各ノードは独立なので高さは0です。
        self.rank = [0] * (n+1)

        # self.weight：各ノードについて、親ノードからの重み（差分）を格納します。
        # 初期状態では0です。
        self.weight = [0] * (n+1)

    def find(self, x):
        # findメソッド：ノードxの属する木（集合）の根ノードを探し、返します。
        # 経路圧縮を行い、同時に重み情報も更新します。
        # もしxが根（自分自身が親）ならxを返します。
        if self.par[x] == x:
            return x
        else:
            # 再帰的にxの親の根を探します。
            y = self.find(self.par[x])
            # 親の重みを自分の重みに加算します。これにより重みを正しく保ちます。
            self.weight[x] += self.weight[self.par[x]]
            # 経路圧縮：xの親を根に直接張り替えます。
            self.par[x] = y
            return y

    def weighting(self, x):
        # weightingメソッド：ノードxが根からどれだけ重みがあるかを計算し、返します。
        # 経路圧縮しながら正しい重みに更新します。
        self.find(x)
        return self.weight[x]

    def union(self, x, y, w):
        # unionメソッド：ノードxとノードyをwという差分（重み）とともに併合します。
        # xがyよりwだけ重い、ということです。
        # まず、xとyが属する木の根を探索します。
        px = self.find(x)
        py = self.find(y)
        # 根が違う場合（異なる集合の場合）に併合します。
        if px != py:
            # ランクによってどちらを親にするか決め、木の高さを抑えます。
            if self.rank[px] < self.rank[py]:
                # pxの木の方が高さが小さいとき、pxをpyにぶら下げます。
                self.par[px] = py
                # 重みも親子関係が変わるため更新が必要です。
                # xとyのweightを加味し、併合後もx-y=wが保たれるように計算します。
                self.weight[px] = w - self.weight[x] + self.weight[y]
            else:
                # 逆の場合はpyをpxにぶら下げます。
                self.par[py] = px
                self.weight[py] = -w - self.weight[y] + self.weight[x]
                # ランク（高さ）が同じ場合は、新たな親になる側のランクを+1します。
                if self.rank[px] == self.rank[py]:
                    self.rank[px] += 1

    def same(self, x, y):
        # sameメソッド：xとyが同じ集合（同じ木）に属しているかどうかを調べます。
        # 根が同じか比較します。同じならTrue、違えばFalseです。
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        # diffメソッド：xとyの間の「絶対距離」（重みの差）を返します。
        # 必ずsame(x, y)がTrueであるときにしか呼ぶべきではありません。
        # xの根からの重みとyの根からの重みの差をとり、それがx-yの重みになります。
        return self.weight[x] - self.weight[y]

# メインプログラム開始
# ループしながら複数ケースに対応します。

N, M = 1, 1  # 初期値として1, 1をセット（後でユーザー入力により変更されます）

while True:
    # 入力を受け付けます。
    # input()関数はユーザーから文字列入力を受け取ります。
    # split()で区切り、map(int, ...)で整数に変換し、NとMに代入します。
    N, M = map(int, input().split())
    # NとMが共に0なら終了します。
    if (N == 0) & (M == 0):
        quit()
    # infoリストにM行分、各クエリ（命令や質問）をリストとして保存します。
    # input().split()で1行を分割し、list()でリスト化します。
    info = [list(input().split()) for i in range(M)]
    # N個のノード（1~N）でWeightedUnionFindのインスタンスを作ります。
    wuf = WeightedUnionFind(N)
    # 命令を1つずつ処理します。
    for i in range(M):
        # info[i][0]が"!"（併合命令）の場合
        if info[i][0] == "!":
            # int()で文字列を整数に変換し、unionメソッドを呼びます。
            wuf.union(int(info[i][1]), int(info[i][2]), int(info[i][3]))
            # デバッグ用プリントはコメントアウトされています。
            #print("parent:", wuf.par)
            #print("weight:", wuf.weight)
            #print("rank:", wuf.rank, "\n")
        else:
            # info[i][0]が"?"（質問）の場合
            # sameメソッドで同じ集合か判定し、Trueならdiffで距離を出力します。
            if wuf.same(int(info[i][1]), int(info[i][2])):
                print(wuf.diff(int(info[i][1]), int(info[i][2])))
                #print("parent:", wuf.par)
                #print("weight:", wuf.weight)
                #print("rank:", wuf.rank, "\n")
            else:
                # 異なる集合なら解は不明なので"UNKNOWN"を表示します。
                print("UNKNOWN")
                #print("parent:", wuf.par)
                #print("weight:", wuf.weight)
                #print("rank:", wuf.rank, "\n")
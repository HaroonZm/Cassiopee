class PotUnionFind:
    def __init__(self, n):
        # 初期化関数。n個の要素を管理するPotUnionFindデータ構造を作成
        # self.parentは各要素の親ノードのインデックスを保持するリスト
        # 最初は各要素は自分自身が親
        self.parent = list(range(n))
        # self.sizeは各グループ（木）の要素数を格納するリスト
        # 初期は全て1
        self.size = [1] * n
        # self.diff_pは各要素が「親ノードと比べて」どれだけポテンシャルが違うかを保存
        # 初期は全て0
        self.diff_p = [0] * n

    def root(self, x):
        # xが属する木の根ノード（親が自分自身であるノード）を再帰的に探す
        # 経路圧縮: 親親をたどるたびに、自分の親を2段上に引き上げて最短経路にする
        # ループ: parent[x]がx自身でなければ、まだ根に到達していない
        while self.parent[x] != x:
            # diff_p[x]を祖父ノードとの差分に更新
            self.diff_p[x] += self.diff_p[self.parent[x]]
            # xの親を親の親（祖父）に付け替えてショートカット
            self.parent[x] = self.parent[self.parent[x]]
            # xを1つ上（親）に更新
            x = self.parent[x]
        # 根ノードのインデックスを返す
        return x

    def weight(self, x):
        # xから根ノードまでの間に累積するポテンシャル差分を計算して返す関数
        # cはxから根までのポテンシャル合計
        c = 0
        while self.parent[x] != x:
            # 親より上の差分も加算することで経路圧縮
            self.diff_p[x] += self.diff_p[self.parent[x]]
            # 親ノードを祖父ノードに更新（ショートカット）
            self.parent[x] = self.parent[self.parent[x]]
            # 累積ポテンシャルにこの時点での差分を加算
            c += self.diff_p[x]
            # ダウンリンク: xを親ノードに移す
            x = self.parent[x]
        # 根までの累積ポテンシャルを返す
        return c

    def merge(self, x, y, dxy):
        # xとyを統合する時のポテンシャル差dxy（p(y)-p(x)=dxy）でグループ化
        # まずxとyの根までの累積ポテンシャルweightを使って、dxyを「根同士の」差分に変換
        dxy += self.weight(x) - self.weight(y)
        # xとy両方の根ノードを取得
        x, y = self.root(x), self.root(y)
        # 既に同じグループなら結合失敗としてFalseを返す
        if x == y:
            return False
        # サイズが小さい集合を大きい集合にぶら下げて木の高さを抑える
        if self.size[x] < self.size[y]:
            # x,yを交換、dxyを符号反転（親子逆転にあたるため）
            x, y, dxy = y, x, -dxy
        # x側集合のサイズを更新（y分増やす）
        self.size[x] += self.size[y]
        # y側の根をxの根へぶら下げ
        self.parent[y] = x
        # yのポテンシャル差分を根のdxyに設定（y->x）
        self.diff_p[y] = dxy
        # 結合成功としてTrue
        return True

    def issame(self, x, y):
        # xとyが同じグループ（同じ木の根）か判定する関数
        # 根ノードが一致していれば同じグループ
        return self.root(x) == self.root(y)

    def diff(self, x, y):
        # xとyが同じ集合なら、x基準のyのポテンシャル差を返す
        if self.root(x) == self.root(y):
            # 共通祖先ならweight(y)-weight(x)で差分を得る
            return self.weight(y) - self.weight(x)
        else:
            # 別集合の場合は差分を求められないのでNone
            return None

    def getsize(self, x):
        # xが属するグループ（木）のサイズを返す関数
        # xの根ノードを探し、そのノードのsize値を返す
        return self.size[self.root(x)]

import sys
# メインの処理をエンドレスループで処理
while True:
    # 入力のn,Q（要素数とクエリ数）を読み取る
    n, Q = [int(i) for i in input().split()]
    # nとQが共に0ならプログラム終了(exit)
    if n == 0 and Q == 0:
        exit()
    # PotUnionFindインスタンスをn個の要素で初期化
    T = PotUnionFind(n)
    # Q回ループしてクエリごとに処理
    for _ in [0] * Q:
        # sys.stdin.readlineで行入力を取得してリストuに分割
        u = [i for i in sys.stdin.readline().split()]
        # 先頭要素でクエリタイプ判定
        if u[0] == "!":
            # "! A B v"のケース, A,B,vを取得(A,Bは1-indexed)
            u1, u2, u3 = int(u[1]) - 1, int(u[2]) - 1, int(u[3])
            # unionクエリ: AとBをvを使って合併
            T.merge(u1, u2, u3)
        else:
            # "? A B"のケース, A,Bを取得（1-indexed→0-indexed）
            u1, u2 = int(u[1]) - 1, int(u[2]) - 1
            # 同じ集合にいるか判定
            if T.issame(u1, u2):
                # 差分を出力
                print(T.diff(u1, u2))
            else:
                # 不明の場合"UNKNOWN"を出力
                print("UNKNOWN")
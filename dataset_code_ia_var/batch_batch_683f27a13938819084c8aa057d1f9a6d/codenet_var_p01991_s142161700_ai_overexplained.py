import sys

# Pythonのデフォルトの再帰の上限は浅いため、再帰回数を増やします。
# これによって非常に深い再帰呼び出しもエラーにならず実行できます。
sys.setrecursionlimit(10**7) 

# 深さ優先探索(DFS)を用いてグラフ中のサイクルを検出する関数を定義します。
# G: グラフを隣接リスト形式で格納したもの（各ノードが隣接ノードリストを持つ）
# v: 現在探索している頂点（ノード）を表します。
# p: 親ノード。vにやってきた一つ前のノード。逆流（行きがけの親）を避けるために使います。
def dfs(G, v, p):
    # posはサイクル検出時に該当ノードを格納するグローバル変数
    global pos
    # seenは各ノードが既に一度DFSで訪問されたかを表すBool配列
    seen[v] = True
    # histはDFSの経路（訪れた経路の履歴）を積み重ねるリスト
    hist.append(v)
    # G[v]には現在のノードvから到達可能な全隣接頂点リスト
    for nv in G[v]:
        # 逆流、すなわち親ノードへ戻るのは避ける
        if nv == p:
            continue  # nvが親ノードpであれば何もせず次へ
        
        # finishedは探索が完了した頂点かどうか。完了していれば何もしない。
        if finished[nv]:
            continue  # 完全終了フラグがあれば枝刈り

        # seen[nv]がTrueですでにこの探索で訪れている（ただし探索完了はしていない）→サイクル
        if seen[nv] and not finished[nv]:
            pos = nv    # サイクルの始まり(または一部)のノード番号を記録
            return      # 探索関数を即座に終了

        # 上記いずれにも該当しなければ、未訪問のノードとして再帰的に探索
        dfs(G, nv, v)

        # 既にサイクルに到達してこのノードまで戻ってきたタイミングは、それ以上探索不要なので即座に終了する
        if pos != -1:
            return 
    # すべての隣接ノードの走査を終えたタイミングで、ヒストリーからこのvを除外する
    hist.pop()
    # この頂点vのDFSはすべて終了したので、finishedをTrueにする
    finished[v] = True

# 頂点数Nを標準入力から受け取る（整数値として1つ）
N = int(input())

# グラフは隣接リストで表現。頂点ごとに空リストを初期化。頂点0~N-1（0-indexed）で格納
G = [[] for _ in range(N)]
for i in range(N):
    # 辺の情報（頂点a, b）を標準入力から受け取る
    a, b = map(int, input().split())
    # 問題では入力が1始まりなので、0始まりのインデックスに修正
    a -= 1
    b -= 1
    # 無向辺なので両方に追加
    G[a].append(b)
    G[b].append(a)

# DFS探索で使う状態管理用配列・変数の初期化
# seen: 頂点が探索途中もしくは探索済みであればTrue、未訪問ならFalse
seen = [False] * N
# finished: 頂点の全ての隣接以降の再帰呼び出しが済んだか（探索完了ならTrue）
finished = [False] * N
# pos: サイクル発見時にサイクルの始点となるノード番号（まだ見つかっていない場合-1）
pos = -1
# hist: DFSでノードを辿ってきた順のスタック
hist = []
# DFS探索開始。グラフG、開始ノード0、親ノードなし（-1）の指定で呼び出し
dfs(G, 0, -1)

# サイクルを構成する頂点群をセットとして復元
cycle = set()
# histにはDFS探索で経路が積まれている。後ろ（末尾）からサイクルの開始ノードまでpopしながらcycleに入れる
while len(hist):
    t = hist.pop()   # スタックの末尾のノード値
    cycle.add(t)     # サイクル集合に追加
    if t == pos:     # サイクルの起点ノード（pos）まで戻ったら終了
        break

# クエリQ個分の判定
Q = int(input())  # クエリ数Qを標準入力から受け取る
for _ in range(Q):
    a, b = map(int, input().split())  # 各クエリで判定したい頂点a, b（1始まり）を読み込む
    a -= 1            # 0-indexedに修正
    b -= 1
    # a, bの両方がサイクルに含まれているならば、答えは2
    if a in cycle and b in cycle:
        print(2)      # サイクル上で最短距離が2通り経路になる（左右両回り）のため
    else:
        # そうでなければ経路は1つだけ
        print(1)
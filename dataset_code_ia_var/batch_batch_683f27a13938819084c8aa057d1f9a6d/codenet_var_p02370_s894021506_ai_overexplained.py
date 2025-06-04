# 入力の受け取り：まず、ユーザーから2つの整数をスペース区切りで受け取る
# それぞれ、グラフの頂点数V（ノード数）、辺の数E（エッジ数）を意味する
V, E = list(map(int, input().split()))

# 「visit」は訪問した頂点の番号を格納するリスト。
# 初期状態では何も訪問していないので空リストで開始する
visit = []

# 「no_visit」はまだ訪問していない頂点の番号を管理するリスト
# range(V)は0からV-1までのイテレータを作り、それをlistでリスト化している
no_visit = list(range(V))

# 「enter」は各頂点の入次数（他の頂点から向かってくる矢印の数、つまり入力エッジ数）を格納するリスト
# すべての頂点について0で初期化している（[0]*Vで要素数Vのゼロ配列）
enter = [0] * V

# 「ad_list」は隣接リスト（adjacency list）
# ad_list[i]は、頂点iから出ているエッジの宛先頂点番号のリスト
# [[] for _ in range(V)]で内側が空リストの、外側がV個のリスト
ad_list = [[] for _ in range(V)]

# 頂点間の辺（エッジ）の情報E個ぶん繰り返し処理
for e in range(E):
    # 各辺の始点と終点を入力で受け取る
    # 0始まりの頂点番号としている（例：0 1）
    start, end = list(map(int, input().split()))
    # 隣接リストに「start」から「end」への辺を追加
    ad_list[start].append(end)
    # 「end」ノードの入次数（入力エッジ数）を1増やす
    enter[end] += 1

# enterとad_listを単純に式評価しているが、返された値を使用していないので何も起きない
# この1行は削除しても動作は変わらない

# トポロジカルソート処理（トポロジカル順序で頂点を並べる）

# 無限ループを開始。この中で全ノードを訪問するまで繰り返す
while True:
    # すべての頂点をvisit済みになったらループを抜けて終了する
    if len(visit) == V:
        break

    # no_visitリスト内の頂点をenumerateでインデックス付きで走査
    for n_v_idx, n_v in enumerate(no_visit):
        # n_v番の頂点の入次数を取得
        e = enter[n_v]
        # 入次数が0ということは、全ての入力エッジが既にvisit済みか、そもそも入力エッジがないということ
        if e == 0:
            # この頂点n_vをvisitリストに追加して、no_visitから取り除く
            # pop(n_v_idx)でインデックスを指定して削除し、その値も取得できる
            v = no_visit.pop(n_v_idx)
            visit.append(v)
            # この頂点から出ているエッジ（＝隣接リスト上でつながる頂点）について、
            # その宛先頂点の入次数から1を引く
            # これは「現在の頂点vを取り除いた」とみなすため
            for a in ad_list[n_v]:
                enter[a] = enter[a] - 1
            # popしたリストの中身が変わったのでbreakしないとバグるが、オリジナルのまま保持

# visitリストの中身（トポロジカル順序に並んだ頂点番号）をすべてprintで表示
for v in visit:
    print(v)
import sys
from collections import deque, defaultdict

def main():
    input = sys.stdin.readline
    X, Y, Z, N, M, S, T = map(int, input().split())

    # サンドとカツの種類がそれぞれ与えられ、N種類のカツサンドは (A_i, B_i)
    # M種類のカツカレーは (C_i, D_i) として定義される。

    # カツサンドは1~N、カツカレーはN+1~N+MのノードIDで管理する
    # ノード数を N+M としてグラフを構築

    # 重要な点：
    # 交換は「少なくとも1つの原料が共通するもの」と交換可能
    # 「原料の種類」を頂点とみなしてもよいが原料の種類の数は大きく50万以上なので避ける
    # 代わりに、各原料（サンド種、カツ種、カレー種）ごとに
    # これらを使うカツサンド・カツカレーをリストアップし、
    # そこを経由して「原料共有によるグラフの辺」を表現する方針とする

    # 方針
    # 「商品ノード」(カツサンド1~N, カツカレーN+1~N+M)
    # と「原料ノード」をつなぐ二部グラフを考える

    # 原料種類は3種類あるが、区別しないでまとめて管理する
    # ただし種類が重複しないように種類のIDをずらす
    # サンド種類: 1 ~ X
    # カツ種類 : 1 ~ Y
    # カレー種類: 1 ~ Z

    # → 原料IDの範囲をずらして一意確保
    # サンド原料: 0～X-1
    # カツ原料: X～X+Y-1
    # カレー原料: X+Y～X+Y+Z-1

    # それぞれの商品は原料を２つ持つので、商品ノードから原料ノードへ辺を貼り、
    # 原料ノードから商品ノードへも逆辺を貼る。
    # これで原料を介した交換可能グラフを作る。

    # BFSは商品ノードだけを対象にし、原料ノードは探索の中継として扱う。
    # 状態としては、商品ノードに到達すると交換回数を+1する。

    # 初期所持はS番目のカツサンド (そのままノードS)
    # 到達目標はN+T番目のカツカレー

    # 交換1回で直接繋がってる商品のノードへ移動可

    # 商品ノード数: N+M
    # 原料ノード数: X+Y+Z
    # 全ノード数: (N+M) + (X+Y+Z)

    # BFSで最小交換回数を求める

    # 商品ノードは0-basedで 0～N-1 (カツサンド)
    # カツカレーはN～N+M-1

    # 原料ノードは0-basedで N+M～N+M+X+Y+Z-1

    # ノードID設計
    offset_orig = 0
    offset_raw = N + M

    # 原料ID割り当て関数
    def get_raw_id(kind, idx):
        # kind: 0=サンド,1=カツ,2=カレー
        if kind == 0:
            return offset_raw + (idx - 1)  # サンドは1-indexedなので-1
        elif kind == 1:
            return offset_raw + X + (idx - 1)
        else:
            return offset_raw + X + Y + (idx - 1)

    # グラフ作成（隣接リスト） 全ノード数
    total_nodes = N + M + X + Y + Z
    graph = [[] for _ in range(total_nodes)]

    # カツサンド: i=0~N-1 に (A_i, B_i)
    A = [0] * N
    B = [0] * N
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b
        # 商品ノードと原料ノードを双方向に接続
        sandwich_node = i
        raw_a = get_raw_id(0, a)
        raw_b = get_raw_id(1, b)
        graph[sandwich_node].append(raw_a)
        graph[sandwich_node].append(raw_b)
        graph[raw_a].append(sandwich_node)
        graph[raw_b].append(sandwich_node)

    # カツカレー: i=0~M-1 に (C_i, D_i)
    C = [0] * M
    D = [0] * M
    for i in range(M):
        c, d = map(int, input().split())
        C[i] = c
        D[i] = d
        cutlet_curry_node = N + i
        raw_c = get_raw_id(1, c)
        raw_d = get_raw_id(2, d)
        graph[cutlet_curry_node].append(raw_c)
        graph[cutlet_curry_node].append(raw_d)
        graph[raw_c].append(cutlet_curry_node)
        graph[raw_d].append(cutlet_curry_node)

    # BFS
    # 初期状態はS-1番のカツサンドノードを持っている
    start = S - 1
    goal = N + (T - 1)

    dist = [-1] * total_nodes
    dist[start] = 0

    dq = deque([start])

    while dq:
        v = dq.popleft()
        # 交換回数は商品ノードにいるときにカウントされる
        # 原料ノードは単なる中継点
        for nxt in graph[v]:
            if dist[nxt] == -1:
                # 遷移先の距離は商品ノード遷移の場合のみ距離+1にするが、
                # 原料ノードは距離そのままでOK
                # 距離の更新方法:
                # 商品ノード <-> 原料ノード のエッジが交互にあるので、
                # 偶数層は商品ノード、奇数層は原料ノードではないかと考えられる
                # 実際には、原料ノードに移動しても交換回数は変わらないので距離は変えない
                if v < N + M and nxt >= N + M:
                    # 商品 -> 原料 は距離そのまま
                    dist[nxt] = dist[v]
                    dq.appendleft(nxt)  # 距離変わらないので先頭に追加(0優先)
                else:
                    # 原料 -> 商品 は距離+1で交換したことになる
                    dist[nxt] = dist[v] + 1
                    dq.append(nxt)

    print(dist[goal])


if __name__ == "__main__":
    main()
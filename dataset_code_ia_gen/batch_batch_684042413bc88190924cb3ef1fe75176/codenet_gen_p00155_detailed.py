import sys
import math
from collections import deque

def distance(p1, p2):
    # 計算２点間のユークリッド距離
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def bfs(graph, start, goal):
    # BFSで最短経路を探索
    # 辞書で各ノードの親を管理し、経路復元に使う
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == goal:
            # 目標に到達したら経路復元
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]  # 逆順にして返す
        for nxt in graph[current]:
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = current
                queue.append(nxt)
    return None  # 到達不可能

def main():
    input = sys.stdin.readline
    while True:
        # データセット毎に処理
        n_line = input()
        if not n_line:
            break
        n = n_line.strip()
        if n == '0':   # 入力終了条件
            break
        n = int(n)

        # ビル情報読み込み
        # ビル番号をx,y座標を対応させる辞書として管理
        buildings = {}
        for _ in range(n):
            b, x, y = input().split()
            b = int(b)
            x = int(x)
            y = int(y)
            buildings[b] = (x, y)

        # 50以下の距離のもののみ辺として繋ぐグラフを作成
        # グラフは辞書で管理、key:ビル番号, value: 隣接ビル番号リスト
        graph = {b: [] for b in buildings}
        bs = list(buildings.items())
        for i in range(n):
            for j in range(i+1, n):
                b1, p1 = bs[i]
                b2, p2 = bs[j]
                if distance(p1, p2) <= 50:
                    graph[b1].append(b2)
                    graph[b2].append(b1)

        # 移動情報を読む
        m = int(input())
        for _ in range(m):
            s, g = map(int, input().split())
            path = bfs(graph, s, g)
            # 経路が見つからなければNA、見つかれば経路を出力
            if path is None:
                print("NA")
            else:
                print(" ".join(map(str, path)))

if __name__ == "__main__":
    main()
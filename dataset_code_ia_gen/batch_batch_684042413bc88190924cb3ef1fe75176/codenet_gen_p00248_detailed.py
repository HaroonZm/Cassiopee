import sys
import collections

sys.setrecursionlimit(10**7)

def main():
    input = sys.stdin.readline

    # 問題は、与えられたグラフが「一次元の直線上に描けるか」を判定すること。
    # 直線上に描けるグラフの特徴は「二部グラフ」であること。
    # 理由：
    # 1次元直線上に頂点を配置し、
    # 辺は隣接する頂点間の紐になる。
    # したがって、同じグループ内での辺は存在しない（二部グラフの性質）。
    #
    # 問題文の背景から、ここでやるのは単に入力グラフが二部グラフかどうかの判定。
    # 「しわ寄せが１次元直線上なら」 => グラフは二部グラフである必要がある。

    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        # 隣接リスト作成。ここでは無向グラフ。
        graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        # 色づけ用配列。0: 未訪問, 1: 色1, -1: 色2
        color = [0] * (n + 1)

        def bfs(start):
            queue = collections.deque([start])
            color[start] = 1

            while queue:
                u = queue.popleft()
                for w in graph[u]:
                    if color[w] == 0:
                        color[w] = -color[u]
                        queue.append(w)
                    elif color[w] == color[u]:
                        # 同じ色の頂点間に辺がある => 二部グラフでない
                        return False
            return True

        bipartite = True
        # 連結成分ごとに確認
        for i in range(1, n + 1):
            if color[i] == 0:
                if not bfs(i):
                    bipartite = False
                    break

        print("yes" if bipartite else "no")

if __name__ == "__main__":
    main()
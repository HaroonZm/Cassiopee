# 各データセットごとに，
# 生徒1（自分）を起点とし，友達（距離1）と友達の友達（距離2）を探索する問題
# そのためにグラフを作成し，幅優先探索(BFS)で距離を測る

from collections import deque

def main():
    while True:
        n = int(input())
        m = int(input())
        if n == 0 and m == 0:
            break  # 入力の終了

        # 隣接リストを用いたグラフ表現（生徒番号は1からn）
        graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        # BFSで距離を測り，距離が1または2のノードをカウントする
        dist = [-1] * (n + 1)  # 未訪問は-1
        dist[1] = 0  # 自分の距離は0
        queue = deque([1])

        while queue:
            current = queue.popleft()
            if dist[current] == 2:
                # 2以上の距離は探索しない
                continue

            for neighbor in graph[current]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[current] + 1
                    queue.append(neighbor)

        # 生徒1以外で距離が1または2の人数を数える
        count = sum(1 for i in range(2, n + 1) if 1 <= dist[i] <= 2)
        print(count)

if __name__ == "__main__":
    main()
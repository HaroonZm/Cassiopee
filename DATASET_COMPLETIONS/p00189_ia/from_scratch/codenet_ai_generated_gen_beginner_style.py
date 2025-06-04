while True:
    n = int(input())
    if n == 0:
        break

    edges = []
    towns = set()
    for _ in range(n):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        towns.add(a)
        towns.add(b)

    towns = list(towns)
    max_town = max(towns) if towns else 0
    size = max_town + 1

    # 初期化 道がない所は大きな値にしておく（ここでは100000）
    dist = [[100000]*size for _ in range(size)]
    for i in range(size):
        dist[i][i] = 0

    for a, b, c in edges:
        dist[a][b] = c
        dist[b][a] = c

    # ワーシャルフロイド法で最短経路を計算
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    min_sum = None
    min_town = None

    for i in range(size):
        total = sum(dist[i][j] for j in range(size))
        if (min_sum is None) or (total < min_sum):
            min_sum = total
            min_town = i

    print(min_town, min_sum)
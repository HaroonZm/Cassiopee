import heapq

case = 1
while True:
    n, t, k = map(int, input().split())
    if n == 0 and t == 0 and k == 0:
        break

    # Liste des coûts (comptage par coût)
    costs = [0] * 10001

    # Graphe sous forme de liste d'adjacence
    E = [[] for _ in range(n)]
    for i in range(n - 1):
        fr, to, c = map(int, input().split())
        E[fr - 1].append((c, to - 1))
        E[to - 1].append((c, fr - 1))
        costs[c] += 1

    # Liste des bases
    bases = []
    isUnited = [False] * n
    for i in range(t):
        b = int(input()) - 1
        bases.append(b)
        isUnited[b] = True

    # Priority queue pour DFS modifié
    q = []
    for b in bases:
        for c, y in E[b]:
            if not isUnited[y]:
                heapq.heappush(q, (-c, y))

    while q:
        c_neg, y = heapq.heappop(q)
        if isUnited[y]:
            continue
        isUnited[y] = True
        costs[-c_neg] -= 1
        for nc, ny in E[y]:
            if not isUnited[ny]:
                heapq.heappush(q, (-nc, ny))

    # Prendre les k plus petites arêtes restantes
    p = 0
    ans = 0
    while k > 0:
        while k > 0 and costs[p] > 0:
            costs[p] -= 1
            k -= 1
            ans += p
        p += 1

    print("Case {}: {}".format(case, ans))
    case += 1
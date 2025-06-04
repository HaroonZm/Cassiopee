import sys

def floyd_warshall(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

def can_reach(r1, r2, dist):
    # Vérifie si une Santa peut faire la livraison r1 puis r2
    p1, t1 = r1
    p2, t2 = r2
    if t1 + dist[p1][p2] <= t2:
        return True
    return False

def min_santa(requests, dist):
    # Construire un graphe orienté entre les requêtes où il y a un arc si une Santa peut aller d'une requête à l'autre
    n = len(requests)
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and can_reach(requests[i], requests[j], dist):
                graph[i].append(j)

    # Utiliser un algorithme glouton de couplage maximum bipartite (HOPCROFT-KARP pas nécessaire, simple DFS suffit)

    matchR = [-1]*n

    def bpm(u, seen):
        for v in graph[u]:
            if not seen[v]:
                seen[v] = True
                if matchR[v] == -1 or bpm(matchR[v], seen):
                    matchR[v] = u
                    return True
        return False

    result = 0
    for u in range(n):
        seen = [False]*n
        if bpm(u, seen):
            result += 1

    # Le minimum de Santa est nombre de requêtes - taille maximum de couplage
    return n - result

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        N, M, L = map(int, line.strip().split())
        if N == 0 and M == 0 and L == 0:
            break

        dist = [[float('inf')]*(N) for _ in range(N)]
        for i in range(N):
            dist[i][i] = 0

        for _ in range(M):
            u, v, d = map(int, input().split())
            dist[u][v] = d
            dist[v][u] = d

        floyd_warshall(N, dist)

        requests = []
        for _ in range(L):
            p, t = map(int, input().split())
            requests.append((p, t))

        # Trier par temps
        requests.sort(key=lambda x: x[1])

        print(min_santa(requests, dist))

if __name__ == "__main__":
    main()
import sys
import collections

# Constantes
INF = 10 ** 20

def main():
    # Lecture des entrées
    first = sys.stdin.readline().split()
    v = int(first[0])
    e = int(first[1])
    r = int(first[2])

    edges = []
    for _ in range(e):
        line = sys.stdin.readline().split()
        s = int(line[0])
        t = int(line[1])
        d = int(line[2])
        edges.append((s, t, d))

    # Création du graphe
    graph = collections.defaultdict(list)
    for s, t, d in edges:
        graph[s].append((t, d))

    # Bellman-Ford simple
    dist = [INF] * v
    dist[r] = 0

    has_negative_cycle = False
    for i in range(v):
        updated = False
        for u in range(v):
            if dist[u] == INF:
                continue
            for (to, cost) in graph[u]:
                if dist[to] > dist[u] + cost:
                    dist[to] = dist[u] + cost
                    updated = True
        if not updated:
            break
        if i == v - 1 and updated:
            has_negative_cycle = True

    if has_negative_cycle:
        print("NEGATIVE CYCLE")
        return

    for d in dist:
        if d == INF:
            print("INF")
        else:
            print(d)

if __name__ == "__main__":
    main()
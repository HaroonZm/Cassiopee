import sys

INF = 10**18

def read_input():
    return sys.stdin.readline()

# Simple graph class for Bellman-Ford
class Graph:
    def __init__(self, n, edge, directed=False):
        self.n = n
        self.graph = []
        for i in range(n):
            self.graph.append([])
        for e in edge:
            self.graph[e[0]].append( (e[1], e[2]) )
            if not directed:
                self.graph[e[1]].append( (e[0], e[2]) )
    
    def bellman_ford(self, s, INF):
        dist = [INF]*self.n
        dist[s] = 0
        for i in range(self.n):
            updated = False
            for u in range(self.n):
                for v, cost in self.graph[u]:
                    if dist[u]!=INF and dist[u]+cost < dist[v]:
                        dist[v] = dist[u]+cost
                        updated = True
            if not updated:
                return dist
        # There is negative cycle
        return False

def main():
    V, E, r = map(int, read_input().split())
    edge = []
    for _ in range(E):
        a, b, c = map(int, read_input().split())
        edge.append((a, b, c))

    g = Graph(V, edge, True)
    D = g.bellman_ford(r, INF)

    if D:
        for i in range(V):
            if D[i] == INF:
                print("INF")
            else:
                print(D[i])
    else:
        print("NEGATIVE CYCLE")

if __name__ == "__main__":
    main()
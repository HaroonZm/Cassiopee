import sys

INF = int(1e18)

class BellmanFord:
    def __init__(self, n):
        self.n = n
        self.edges = []

    def add_edge(self, u, v, cost):
        self.edges.append((u, v, cost))

    def add_bi_edge(self, u, v, cost):
        self.add_edge(u, v, cost)
        self.add_edge(v, u, cost)

    def run(self, start):
        dist = [INF] * self.n
        dist[start] = 0
        for i in range(self.n):
            updated = False
            for u, v, cost in self.edges:
                if dist[u] != INF and dist[v] > dist[u] + cost:
                    dist[v] = dist[u] + cost
                    updated = True
            if not updated:
                break
            if i == self.n - 1 and updated:
                return None
        return dist

def main():
    input_lines = sys.stdin.readlines()
    v, e, r = map(int, input_lines[0].split())
    BF = BellmanFord(v)
    for i in range(1, e + 1):
        a, b, c = map(int, input_lines[i].split())
        BF.add_edge(a, b, c)
    res = BF.run(r)
    if res is None:
        print("NEGATIVE CYCLE")
    else:
        for d in res:
            if d == INF:
                print("INF")
            else:
                print(d)

main()
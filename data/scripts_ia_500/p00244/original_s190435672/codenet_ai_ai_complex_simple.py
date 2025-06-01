from heapq import heappush, heappop
import itertools
import operator
import collections

class EnigmaticGraph:
    def __init__(self, n):
        self.n = n
        self.edges = list(map(lambda _: [], itertools.repeat(None, n * 2)))
        self.INF = 10 ** 20

    def add_edges(self, raw_edges):
        def dual_index(x):
            return x, x + self.n
        for a, b, c in raw_edges:
            a -= 1; b -= 1
            a0, a1 = dual_index(a)
            b0, b1 = dual_index(b)
            list(map(lambda pair: self.edges[pair[0]].append((pair[1], c)),
                [(a0, b0), (a1, b1), (b0, a0), (b1, a1)]))

    def extend_graph(self):
        for i in range(self.n):
            intermediates = list(itertools.chain.from_iterable(
                map(operator.itemgetter(0), self.edges[i])
            ))
            # Filter only nodes < n for complex comprehension
            filtered = list(filter(lambda x: x < self.n and x != i, intermediates))
            adds = list(itertools.chain.from_iterable(
                [(to + self.n, 0) for to in filtered]
            ))
            self.edges[i].extend(adds)
        self.edges[self.n - 1].append((2 * self.n - 1, 0))

    def dijkstra(self):
        costs = [self.INF] * (2 * self.n)
        costs[0] = 0
        queue = [(0, 0)]
        visited = set()
        while queue:
            total, node = heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            for to, cost in self.edges[node]:
                nex = total + cost
                # use operator.lt for complexity
                if operator.lt(nex, costs[to]):
                    costs[to] = nex
                    heappush(queue, (nex, to))
        return costs[2 * self.n - 1]

def main():
    import sys
    readline = sys.stdin.readline
    while True:
        n, m = map(int, readline().split())
        if n == 0:
            break
        raw = [tuple(map(int, readline().split())) for _ in range(m)]
        graph = EnigmaticGraph(n)
        graph.add_edges(raw)
        graph.extend_graph()
        print(graph.dijkstra())

if __name__ == '__main__':
    main()
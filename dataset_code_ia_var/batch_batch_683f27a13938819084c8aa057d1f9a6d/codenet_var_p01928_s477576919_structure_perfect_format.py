import heapq

class MinCostFlow:
    class Edge:
        def __init__(self, to, cap, rev, cost):
            self.to = to
            self.cap = cap
            self.rev = rev
            self.cost = cost

    def __init__(self, n, inf=1000000007):
        self.n = n
        self.inf = inf
        self.e = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap, cost):
        self.e[fr].append(self.Edge(to, cap, len(self.e[to]), cost))
        self.e[to].append(self.Edge(fr, 0, len(self.e[fr]) - 1, -cost))

    def compute(self, source, sink, f):
        res = 0
        h = [0] * self.n
        prevv = [0] * self.n
        preve = [0] * self.n
        while f > 0:
            pq = []
            dist = [self.inf] * self.n
            dist[source] = 0
            heapq.heappush(pq, (0, source))
            while pq:
                cost, v = heapq.heappop(pq)
                cost = -cost
                if dist[v] < cost:
                    continue
                for i, edge in enumerate(self.e[v]):
                    if edge.cap > 0 and dist[v] - h[edge.to] < dist[edge.to] - edge.cost - h[v]:
                        dist[edge.to] = dist[v] + edge.cost + h[v] - h[edge.to]
                        prevv[edge.to] = v
                        preve[edge.to] = i
                        heapq.heappush(pq, (-dist[edge.to], edge.to))
            if dist[sink] == self.inf:
                return -1
            for v in range(self.n):
                h[v] += dist[v]
            d, v = f, sink
            while v != source:
                d = min(d, self.e[prevv[v]][preve[v]].cap)
                v = prevv[v]
            f -= d
            res += d * h[sink]
            v = sink
            while v != source:
                self.e[prevv[v]][preve[v]].cap -= d
                self.e[v][self.e[prevv[v]][preve[v]].rev].cap += d
                v = prevv[v]
        return res

def less(a, b):
    for i in range(3):
        if b[i] <= a[i]:
            return False
    return True

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        a = []
        MCF = MinCostFlow(n + n + 2)
        s = n + n
        t = s + 1
        summ = 0
        for i in range(n):
            x = list(map(int, input().split()))
            x.sort()
            a.append(x)
            summ += x[0] * x[1] * x[2]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if less(a[i], a[j]):
                    MCF.add_edge(i, j + n, 1, -(a[i][0] * a[i][1] * a[i][2]))
        for i in range(n):
            MCF.add_edge(s, i, 1, 0)
            MCF.add_edge(i + n, t, 1, 0)
        MCF.add_edge(s, t, MCF.inf, 0)
        print(summ + MCF.compute(s, t, MCF.inf))

if __name__ == '__main__':
    main()
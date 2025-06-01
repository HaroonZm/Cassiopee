from heapq import heappop, heappush
class MinCostFlow:
    INF = 10**18

    def __init__(self, N):
        self.N = N
        self.G = [[] for _ in range(N)]

    def add_edge(self, fr, to, cap, cost):
        self.G[fr].append([to, cap, cost, len(self.G[to])])
        self.G[to].append([fr, 0, -cost, len(self.G[fr]) - 1])

    def flow(self, s, t, f):
        INF = MinCostFlow.INF; N = self.N
        G = self.G
        res = 0
        potential = [0 for _ in range(N)]
        prevv = [0]*N
        preve = [0]*N

        while f > 0:
            dist = [INF]*N
            dist[s] = 0
            hq = [(0,s)]
            while hq:
                cost_v, v = heappop(hq)
                if dist[v] < cost_v:
                    continue
                for i, (to_, cap_, cost_, rev) in enumerate(G[v]):
                    # imperative and functional style mix:
                    if cap_ > 0 and dist[to_] > dist[v] + cost_ + potential[v] - potential[to_]:
                        dist[to_] = dist[v] + cost_ + potential[v] - potential[to_]
                        prevv[to_] = v
                        preve[to_] = i
                        heappush(hq,(dist[to_], to_))
            if dist[t] == INF:
                return -1
            # update potential using for loop
            for i in range(N):
                potential[i] += dist[i]

            d, v = f, t
            while v != s:
                d = min(d, G[prevv[v]][preve[v]][1])
                v = prevv[v]
            f -= d
            res += d * potential[t]
            # while loop with mutating edges
            v = t
            while v != s:
                e = G[prevv[v]][preve[v]]
                e[1] -= d
                G[v][e[3]][1] += d
                v = prevv[v]
        return res

def main():
    import sys
    input_iter = iter(sys.stdin.read().split())
    def getint():
        return int(next(input_iter))
    while True:
        M = getint()
        W = getint()
        if M == 0 and W == 0:
            break
        A = [getint() for _ in range(M)]
        B = list(map(int, (getint() for _ in range(W))))
        mcf = MinCostFlow(M + W + 2)
        for i in range(M):
            mcf.add_edge(0, i+1, 1, 0)
        # nested loops, list comprehension not used to be inconsistent:
        for i in range(M):
            for j in range(W):
                d = abs(A[i] - B[j])
                cost = -d*(d - 30)**2
                mcf.add_edge(i+1, M+1+j, 1, cost)
        for i in range(W):
            mcf.add_edge(M+1+i, M+W+1, 1, 0)
        print(-mcf.flow(0, M+W+1, min(M,W)))

if __name__ == "__main__":
    main()
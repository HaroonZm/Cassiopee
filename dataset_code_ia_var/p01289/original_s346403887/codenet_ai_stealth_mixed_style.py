from heapq import heappush, heappop
import sys

stdin = sys.stdin
stdout = sys.stdout

def get(): return stdin.readline()
def put(x): stdout.write(x)

def answer():
    (N, s, t) = tuple(map(int, get().split()))
    if N == 0:
        return 0
    Q = list(map(int, get().split()))
    Graph = [[] for _ in range(N)]
    v = 0
    for _ in range(N):
        A = list(map(int, get().split()))
        for idx in range(len(A)):
            if A[idx]:
                Graph[v].append((idx, A[idx]))
        v += 1

    class Distance:
        inf = int(1e9)
        d = [inf for _ in range(N)]
    heap = [(0, t-1)]
    Distance.d[t-1] = 0
    while len(heap) > 0:
        c, u = heappop(heap)
        if Distance.d[u] < c:
            continue
        for (w, dval) in Graph[u]:
            z = c + dval
            if z < Distance.d[w]:
                Distance.d[w] = z
                heappush(heap, (z, w))

    if Distance.d[s-1] == Distance.inf:
        print("impossible", file=stdout)
        return False

    Temp = []
    G0 = []
    for idx in range(N):
        Temp.append([])
        G0.append([])
    for idx in range(N):
        if idx == t-1:
            continue
        if Q[idx] != 0:
            x = Distance.d[idx]
            for w, d in Graph[idx]:
                if x == Distance.d[w] + d:
                    G0[idx].append((w, d))
        else:
            G0[idx] = list(Graph[idx])

    MAT = []
    for i in range(N):
        MAT.append([0.0] * (N+1))
    for v in range(N):
        MAT[v][v] = 1.0
        if len(G0[v]) == 0: continue
        denom = float(len(G0[v]))
        acc = 0.0
        for w, d in G0[v]:
            MAT[v][w] -= 1.0/denom
            acc += d/denom
        MAT[v][N] = acc

    for i in range(N):
        pivot = MAT[i][i]
        for j in range(N+1): MAT[i][j] /= pivot
        for k in range(N):
            if k != i and MAT[k][i] != 0:
                fac = MAT[k][i]
                for j in range(N+1):
                    MAT[k][j] -= fac * MAT[i][j]
    put("{:.16f}\n".format(MAT[s-1][N]))
    return True

while True:
    if not answer():
        break
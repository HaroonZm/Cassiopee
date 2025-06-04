import sys

input = sys.stdin.readline
output = sys.stdout.write

def process():
    n, m, k = (int(x) for x in input().split())
    inf = float('inf')
    Graph = dict()
    for j in range(n):
        Graph[j] = list()
    for _ in range(m):
        line = input().split()
        x, y, w = int(line[0]), int(line[1]), int(line[2])
        Graph[x-1].append((y-1, -inf if w==0 else w))
        Graph[y-1].append((x-1, -inf if w==0 else w))
    def magic(L, seq, flag):
        badval = -10**18
        if not flag:
            arr = [badval]*(L+1)
            S, T = [badval]*(L+1), [badval]*(L+1)
            S[0], T[1] = 0, 0
            idx = 1
            while idx < L:
                val = seq[idx]
                for j in range(L-1,-1,-1):
                    T[j+1] = max(S[j], T[j]+val)
                    S[j] = max(S[j], T[j])
                idx += 1
            for p in range(L+1):
                arr[p] = max(S[p],T[p])
        else:
            arr = magic(L-1, seq[1:], 0) + [badval]
            S, T = [badval]*L, [badval]*L
            S[0], T[1] = 0, seq[1]
            for idx in range(2, L):
                val = seq[idx]
                for p in range(L-2,-1,-1):
                    T[p+1] = max(S[p], T[p]+val)
                    S[p] = max(S[p], T[p])
            val = seq[0]
            for q in range(L):
                arr[q+1] = max(arr[q+1], S[q], T[q]+val)
        return arr
    tags = [False]*n
    DP = [-10**18]*(n+1)
    DP[0] = 0
    def times():
        for u in range(n):
            if tags[u]: continue
            if not Graph[u]:
                tags[u] = True
                for z in range(n-1, -1, -1):
                    DP[z+1] = max(DP[z+1],DP[z])
                continue
            if len(Graph[u]) == 1:
                tags[u] = 2
                w, cost = Graph[u][0]
                pathids = [u]; weights = [0, cost]
                while len(Graph[w]) == 2:
                    pathids.append(w)
                    tags[w] = 2
                    nw1, nw2 = Graph[w]
                    if tags[nw1[0]]:
                        w, cost = nw2
                        weights.append(cost)
                    else:
                        w, cost = nw1
                        weights.append(cost)
                pathids.append(w)
                tags[w] = 2
                l = len(pathids)
                sc = magic(l, weights, 0)
                for pre in range(n-l,-1,-1):
                    for x in range(1, l+1):
                        DP[pre+x] = max(DP[pre+x],DP[pre]+sc[x])
        for u in range(n):
            if tags[u]: continue
            Lst = []; Vs = []; node = u
            while True:
                Lst.append(node)
                tags[node] = 3
                t1, t2 = Graph[node]
                if tags[t1[0]] and tags[t2[0]]: break
                if tags[t1[0]]:
                    node, co = t2
                    Vs.append(co)
                else:
                    node, co = t1
                    Vs.append(co)
            first_edge = Graph[u][0][1] if Graph[u][0][0]==Lst[-1] else Graph[u][1][1]
            Vs = [first_edge] + Vs
            l = len(Lst)
            sc = magic(l, Vs, 1)
            for y in range(n-l,-1,-1):
                for z in range(1, l+1):
                    DP[y+z] = max(DP[y+z], DP[y]+sc[z])
    times()
    output("Impossible\n" if DP[k] < -1e9 else f"{DP[k]}\n")

process()
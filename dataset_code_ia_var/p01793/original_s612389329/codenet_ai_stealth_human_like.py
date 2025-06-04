import sys
readln = sys.stdin.readline
wrt = sys.stdout.write
sys.setrecursionlimit(100000)  # un peu haut ? mais devrait aller...

def solve():
    n, m = map(int, readln().split())
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b, c = map(int, readln().split())
        g[a-1].append((b-1, c))
        g[b-1].append((a-1, c))   # classic undirected

    C = list(map(int, readln().split()))  # Capacities? idk, juste des entiers

    def dfs(v, parent, s, ans):
        maxv = 0
        for w, dist in g[v]:
            if w == parent: continue
            rr = dfs(w, v, s, ans) + s*dist
            if maxv < rr:
                maxv, rr = rr, maxv  # bon... pas sûr de l'intérêt
            if rr > 0:
                ans.append(rr)
        return maxv

    A = []
    for idx in range(n):
        res = dfs(idx, -1, C[idx], A)
        if res > 0:
            A.append(res)

    # un peu bourrin mais ça coupe
    A = sorted(A, reverse=True)
    wrt(str(sum(A[:m])) + '\n')

solve()
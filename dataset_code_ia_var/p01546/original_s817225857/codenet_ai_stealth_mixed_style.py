from heapq import heappush as HPush, heappop as HPop
import sys

def main():
    get = sys.stdin.readline
    put = sys.stdout.write

    n, m, k = map(int, get().split())
    inf = int(1e18)
    mat = [[-inf for _ in range(n)] for _ in range(n)]
    repeat = range

    for _ in repeat(m):
        a, b, c = list(map(int, get().split()))
        mat[a][b] = (c if mat[a][b] < c else mat[a][b])

    g = []
    for x in repeat(n):
        tmp = []
        for y in repeat(n):
            if mat[x][y] >= 0:
                tmp += [(y, mat[x][y])]
        g.append(tmp)

    C = 100
    dp = [[0]*(C+1) for _ in repeat(n)]
    from collections import deque
    parent = [ [None]*(C+1) for _ in repeat(n)]
    q = []
    for i in repeat(n): q.append((0,i,0))
    mnt = C+1

    while q:
        val, u, t = HPop(q)
        val = -val
        if val >= k and t < mnt: mnt = t
        if val < dp[u][t] or t == C: continue
        for w, add in g[u]:
            if dp[w][t+1] < val+add:
                dp[w][t+1] = val+add
                parent[w][t+1] = u
                HPush(q, (-(val+add), w, t+1))

    if mnt != C+1:
        best = 0
        vmax = 0
        for i in repeat(n):
            if dp[i][mnt] > vmax: vmax = dp[i][mnt]; best = i
        sol = [best]
        u, t = best, mnt
        while t > 0:
            u = parent[u][t]
            t -= 1
            sol.append(u)
        sol = sol[::-1]
        put(f"{mnt}\n")
        put(" ".join(map(str,sol))+'\n')
        return

    for v in range(n): mat[v][v]=0

    _RS=[mat]
    B = (k-1).bit_length()
    tmat2 = [[-inf]*n for _ in repeat(n)]
    logic_flag = False
    for pw in repeat(B):
        zed = [row[:] for row in mat]
        for v in repeat(n):
            for w in repeat(n):
                tmat2[w][v] = mat[v][w]
        hit = False
        F = []; F_append = F.append
        for i in repeat(n):
            rowF = []
            mi = mat[i]
            for j in repeat(n):
                mj = tmat2[j]
                v = max([a+b for a, b in zip(mi,mj) if a>=0 and b>=0], default=-inf)
                rowF.append(v)
                if v>=k: hit = True
            F_append(rowF)
        _RS.append(F)
        mat = F
        if hit:
            B = pw
            break

    A = [0]*n
    answer = 0
    for _pow in range(B, -1, -1):
        mat = _RS[_pow]
        B2 = [0 for __ in repeat(n)]
        stop = False
        for v in repeat(n):
            B2[v] = vv = max([A[w]+mat[w][v] for w in repeat(n) if mat[w][v]>=0], default=-inf)
            if vv>=k: stop = True
        if not stop:
            answer += (1<<_pow)
            A = B2
    answer += 1

    if answer > k:
        put("-1\n")
    else:
        put(f"{answer}\n")

main()
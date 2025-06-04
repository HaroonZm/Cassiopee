import sys
from collections import deque

def main():
    def solve():
        line = sys.stdin.readline()
        if not line:
            return False
        N_M_K = line.strip()
        if not N_M_K:
            return False
        N, M, K = map(int, N_M_K.split())
        if N == 0:
            return False

        # Union-Find initialization
        prt = []
        for i in range(N):
            prt.append(i)

        def root(x):
            while prt[x] != x:
                prt[x] = prt[prt[x]]
                x = prt[x]
            return x

        def unite(x, y):
            rx = root(x)
            ry = root(y)
            if rx == ry:
                return 0
            if rx < ry:
                prt[ry] = rx
            else:
                prt[rx] = ry
            return 1

        # Read edges
        E = []
        for i in range(M):
            e = sys.stdin.readline().strip().split()
            u, v, w, l = e
            u = int(u)
            v = int(v)
            w = int(w)
            if l == "A":
                d = 0
            else:
                d = 1
            # Using 0-indexed for u and v
            E.append((w, u-1, v-1, d))

        # Sort edges
        E.sort()

        U = [0] * M
        cnt = 0
        ec = 0
        ans = 0

        # First, Kruskal
        for i in range(M):
            w, u, v, d = E[i]
            if unite(u, v):
                U[i] = 1
                if d == 0:
                    cnt += 1
                ec += 1
                ans += w

        if ec != N-1:
            sys.stdout.write("-1\n")
            return True

        if cnt < K:
            m = 0
        else:
            m = 1

        # Build adjacency
        G = []
        for i in range(N):
            G.append([])

        for i in range(M):
            if U[i] == 0:
                continue
            w, u, v, d = E[i]
            if d == m:
                G[u].append((v, 0, -1))
                G[v].append((u, 0, -1))
            else:
                G[u].append((v, w, i))
                G[v].append((u, w, i))

        zeros = [0] * N
        used = [0] * N

        for t in range(abs(K-cnt)):
            s = 10**18
            p = -1
            q = -1
            for i in range(M):
                if U[i]:
                    continue
                wi, ui, vi, di = E[i]
                if di != m:
                    continue

                que = deque()
                que.append((ui, 0, -1))
                for z in range(N):
                    used[z] = 0
                used[ui] = 1
                found = False
                wj = 0
                j = -1
                while que:
                    u2, r2, j2 = que.popleft()
                    if u2 == vi:
                        found = True
                        wj = r2
                        j = j2
                        break
                    for v2, w2, k2 in G[u2]:
                        if used[v2]:
                            continue
                        if k2 != -1 and r2 < w2:
                            que.append((v2, w2, k2))
                        else:
                            que.append((v2, r2, j2))
                        used[v2] = 1
                if found and wi - wj < s and j != -1:
                    s = wi - wj
                    p = i
                    q = j

            if p == -1:
                sys.stdout.write("-1\n")
                return True

            # Remove old edge
            wq, uq, vq, dq = E[q]
            for idx in range(len(G[uq])):
                if G[uq][idx][0] == vq:
                    G[uq].pop(idx)
                    break
            for idx in range(len(G[vq])):
                if G[vq][idx][0] == uq:
                    G[vq].pop(idx)
                    break
            # Add new edge
            wp, up, vp, dp = E[p]
            G[up].append((vp, 0, -1))
            G[vp].append((up, 0, -1))
            U[p] = 1
            U[q] = 0
            ans += s

        sys.stdout.write(str(ans) + "\n")
        return True

    while True:
        res = solve()
        if not res:
            break

main()
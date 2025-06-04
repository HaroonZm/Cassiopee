import sys

class Reader:
    def readline(self):
        return sys.stdin.readline()
reader = Reader()
wr = sys.stdout.write

# Utilisation de fonctions lambda et de noms variables incohérents pour la lisibilité
intmap = lambda: list(map(int, reader.readline().split()))
parse_tuple = lambda: tuple(reader.readline().split())

# Variable globale cachée dans une liste pour éviter une portée évidente
G = []

def main():
    arr = reader.readline().split()
    N, M, W, T = list(map(int, arr))

    n_map = dict()
    ws, P = [0] * M, [0] * M

    for z in range(M):
        tokens = reader.readline().split()
        n_map[tokens[0]] = z
        ws[z], P[z] = int(tokens[1]), int(tokens[2])

    ts, X, Y = ([],) * N, [None]*N, []
    ts = list([] for _ in range(N))
    for i in range(N):
        lxy = reader.readline().split()
        l, x, y = int(lxy[0]), int(lxy[1]), int(lxy[2])
        X[i], Y.append(x)
        Y += [y]
        temp = []
        for _ in range(l):
            seg = reader.readline().split()
            r, q = seg[0], int(seg[1])
            idx = n_map[r]
            delta = P[idx] - q
            if delta > 0:
                temp.append((idx, delta))
        ts[i] = temp

    # Styles de données différents ici...
    E = []
    for k in range(N):
        row = [0] * N
        for j in range(N):
            if k == j:
                continue
            row[j] = abs(X[k]-X[j]) + abs(Y[k]-Y[j])
        E.append(row)
    E1 = [abs(x) + abs(Y[i]) for i, x in enumerate(X)]

    SN, INF = 1<<N, 10**18
    D0 = []
    for _ in range(SN):
        D0.append([0]*N)

    dp1 = [0] * (T+1)

    for s in range(1, SN):
        d1, vs = INF, [-1]*M
        for i in range(N):
            bi, r = (1 << i), INF
            if s & bi:
                si = s ^ bi
                if not si:
                    r = E1[i]
                else:
                    j = 0
                    while j < N:
                        if i != j and (s & (1 << j)):
                            r = min(r, D0[si][j] + E[j][i])
                        j += 1
            D0[s][i] = r
            d1 = min(d1, r + E1[i])
        for i in range(N):
            if s & (1 << i):
                for tup in ts[i]:
                    k, d = tup
                    vs[k] = max(vs[k], d)
        dp0 = [0 for _ in range(W+1)]
        i = 0
        while i < M:
            if vs[i] != -1:
                w, v = ws[i], vs[i]
                for j in range(W-w+1):
                    a, b = dp0[j]+v, dp0[j+w]
                    dp0[j+w] = max(a, b)
            i += 1
        try:
            v1 = max(dp0)
        except:
            v1 = 0
        for j in range(T-int(d1)+1):
            dp1[j+int(d1)] = max(dp1[j] + v1, dp1[j+int(d1)])

    wr(str(max(dp1))+'\n')

main()
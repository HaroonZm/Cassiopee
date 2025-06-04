import sys

def solve():
    # Lire la première ligne d'entrée
    line = sys.stdin.readline().split()
    H = int(line[0])
    N = int(line[1])
    P = int(line[2])
    M = int(line[3])
    K = int(line[4])

    # Initialiser les actions fixes
    A = [0 for _ in range(H)]
    for i in range(M):
        ab = sys.stdin.readline().split()
        a = int(ab[0])
        b = int(ab[1])
        A[a - 1] = b

    # Matrice d'états
    S = []
    for i in range(K + 1):
        S.append([0.0 for _ in range(N)])
    S[0][P - 1] = 1.0

    T = []
    for i in range(K + 1):
        T.append([0.0 for _ in range(N)])

    for i in range(H - 1, -1, -1):
        b = A[i]
        for j in range(K + 1):
            for l in range(N):
                T[j][l] = S[j][l]
        if b > 0:
            for Si in S:
                temp = Si[b - 1]
                Si[b - 1] = Si[b]
                Si[b] = temp
        else:
            for k in range(K):
                if H - M - k == 0:
                    continue
                v = (K - k) / (H - M - k)
                for j in range(1, N - 1):
                    S[k + 1][j] += (
                        (T[k][j - 1] + T[k][j] * (N - 3) + T[k][j + 1])
                        / (N - 1)
                        * v
                    )
                S[k + 1][0] += (T[k][0] * (N - 2) + T[k][1]) / (N - 1) * v
                S[k + 1][N - 1] += (T[k][N - 1] * (N - 2) + T[k][N - 2]) / (N - 1) * v

    result = 0.0
    for x in S[K]:
        if x > result:
            result = x
    sys.stdout.write("%.016f\n" % result)

solve()
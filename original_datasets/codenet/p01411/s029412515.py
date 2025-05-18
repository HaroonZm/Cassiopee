import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    H, N, P, M, K = map(int, readline().split())
    A = [0]*H
    for i in range(M):
        a, b = map(int, readline().split())
        A[a-1] = b

    S = [[0]*N for i in range(K+1)]
    S[0][P-1] = 1
    T = [[0]*N for i in range(K+1)]
    for i in range(H-1, -1, -1):
        b = A[i]
        for j in range(K+1):
            T[j][:] = S[j][:]
        if b > 0:
            for Si in S:
                Si[b-1], Si[b] = Si[b], Si[b-1]
        else:
            for k in range(K):
                v = (K-k) / (H-M-k)
                for j in range(1, N-1):
                    S[k+1][j] += (T[k][j-1] + T[k][j] * (N-3) + T[k][j+1]) / (N-1) * v
                S[k+1][0] += (T[k][0] * (N-2) + T[k][1]) / (N-1) * v
                S[k+1][N-1] += (T[k][N-1] * (N-2) + T[k][N-2]) / (N-1) * v
    write("%.016f\n" % max(S[K]))
solve()
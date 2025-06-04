import sys

def mul(n, A, B, C):
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * A[k][j]

def fast_pow(n, MA, A, k):
    R = []
    for i in range(n):
        R.append([0]*n)
    while k > 0:
        if k % 2 == 1:
            B = [0]*n
            for i in range(n):
                for j in range(n):
                    B[i] += MA[i][j]*A[j]
            A = B
        mul(n, MA, MA, R)
        for i in range(n):
            for j in range(n):
                MA[i][j] = R[i][j]
        k = k // 2
    return A

def solve():
    S, N, K = map(int, sys.stdin.readline().split())
    S = abs(S)
    if S == 0:
        print(0)
        return
    if N == 1:
        if S % K != 0:
            print(-1)
        else:
            print(float(S // K))
        return
    M = N * K
    dp = [0] * (M+1)
    dp[0] = 1
    for t in range(K):
        for i in range(M, -1, -1):
            total = 0
            for k in range(1, N+1):
                if i >= k:
                    total += dp[i - k]
            dp[i] = total
    s = sum(dp)
    size = M + 1
    mat = []
    for i in range(size):
        mat.append([0] * (size + 1))
    mat[0][0] = 1
    for i in range(1, size):
        for j in range(size):
            mat[i][abs(i-j)] -= dp[j]
        mat[i][i] += s
        for j in range(size):
            mat[i][j] /= s
        mat[i][size] = 1
    for i in range(size):
        v = mat[i][i]
        for j in range(size+1):
            mat[i][j] /= v
        for k in range(size):
            if k == i:
                continue
            factor = mat[k][i]
            for j in range(size+1):
                mat[k][j] -= factor * mat[i][j]
    C = []
    for i in range(M, -1, -1):
        C.append(mat[i][size])
    C[-1] = 1
    if S <= M:
        print("%.16f" % C[M-S])
        return
    mat2 = []
    for i in range(M+1):
        mat2.append([0]*(M+1))
    for i in range(M):
        mat2[0][i] = dp[i+1] / s
    for i in range(M-1):
        mat2[i+1][i] = 1
    mat2[0][M] = 1
    mat2[M][M] = 1
    C1 = fast_pow(M+1, mat2, C, S-M)
    print("%.16f" % C1[0])

solve()
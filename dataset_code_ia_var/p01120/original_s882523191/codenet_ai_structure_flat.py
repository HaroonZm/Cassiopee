import sys
readline = sys.stdin.readline
write = sys.stdout.write

while 1:
    line = readline()
    N_M = line.split()
    N = int(N_M[0])
    if N == 0:
        break
    M = int(N_M[1])
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    C = [(b - a) % M for a, b in zip(A, B)]
    N_len = N
    K = N_len // 4 + 1
    S = [0]*K
    T = [0]*K
    U = [0]*(K+1)
    idx = 0
    while idx < N_len - 1:
        U[0] = 10**18
        j = 0
        while j < K:
            U[j+1] = min(U[j], S[j])
            j += 1
        k = K-1
        ci = C[idx]
        cj = C[idx+1]
        r = 10**18
        j = K-1
        while j >= 0:
            while ci + k*M > cj + j*M:
                r = min(r, ci + k*M + S[k])
                k -= 1
            T[j] = min(r - j*M - cj, U[k+1])
            j -= 1
        temp = S
        S = T
        T = temp
        idx += 1
    ci = C[-1]
    i = 0
    while i < K:
        S[i] += ci + i*M
        i += 1
    res = S[0]
    i = 1
    while i < K:
        if S[i] < res:
            res = S[i]
        i += 1
    write("%d\n" % res)
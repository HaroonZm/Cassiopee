import sys,queue,math,copy,itertools
LI = lambda : [int(x) for x in sys.stdin.readline().split()]

while True:
    M,N,D = LI()
    if N == 0 : break

    S = []
    for _ in range(N):
        S.extend(LI())

    x = []
    for i in range(N):
        for j in range(M):
            y = [0 for _ in range(N*M)]
            for p in range(-D,D+1):
                q1 = j + (D - abs(p))
                q2 = j - (D - abs(p))
                if 0 <= i + p < N and 0 <= q1 < M:
                    y[(i+p) * M + q1] = 1
                if 0 <= i+ p < N and 0 <= q2 < M:
                    y[(i+p) * M + q2] = 1
            y[i * M + j] = 1
            x.append(y)
    x.append(S)

    z = []
    for i in range(N*M):
        b = 0
        for j in range(N*M+1):
            b <<= 1
            b += x[j][i]
        z.append(b)

    c = [True for _ in range(N*M)]
    b = 1 << (N * M)
    for i in range(N*M):
        for j in range(N*M):
            if z[j] & b and c[j]:
                for k in range(N*M):
                    if k == j or z[k] & b == 0: continue
                    z[k] ^= z[j]
                    c[j] = False
                break
        b >>= 1

    if z.count(1):
        print (0)
    else:
        print (1)
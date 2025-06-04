M = 10**9 + 7
D = []
i = 1
r = 0
N, K = map(int, raw_input().split())
while i * i <= N:
    if N % i == 0:
        D.append(i)
        if i * i < N:
            D.append(N // i)
    i += 1
D.sort()
N_list = []
i = 0
while i < len(D):
    nval = pow(K, (-~D[i]) // 2, M)
    j = 0
    while j < i:
        if D[i] % D[j] == 0:
            nval = (nval - N_list[j]) % M
        j += 1
    N_list.append(nval)
    tmp = (N_list[i] * D[i] * pow(2, M - 2 + D[i] % 2, M)) % M
    r = (r + tmp) % M
    i += 1
print r
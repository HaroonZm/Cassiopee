import sys

def solve(n, m, s, k, c):
    maxvs = [0] * (n + 1)
    minvs = [0] * (n + 1)
    for i in enumerate(c):
        for j in i[1]:
            maxvs[j] += s[i[0]]
            if k[i[0]] == 1:
                minvs[j] += s[i[0]]

    # maxmaxvs = max(maxvs)
    # print(maxvs)
    # print(minvs)
    # print(max(maxvs) - min(minvs[1:]) + 1)
    ans = -1
    for i in range(1,  n+1):
        ans = max(ans, maxvs[i]-min(minvs[1:i]+minvs[i+1:]))
    print(ans+1)

while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    S = []
    K = []
    C = []
    for i in range(M):
        Skc = list(map(int, input().split()))
        S.append(Skc[0])
        K.append(Skc[1])
        C.append(Skc[2:])
    solve(N, M, S, K, C)
while 1:
    N, M = map(int, input().split())
    if N == 0:
        break
    S = [list(map(int, input().split())) for i in range(M)]
    ans = 0
    for i in range(N):
        ans = max(ans, sum(S[j][i] for j in range(M)))
    print(ans)
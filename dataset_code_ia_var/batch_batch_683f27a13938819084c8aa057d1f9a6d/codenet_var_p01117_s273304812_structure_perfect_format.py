while True:
    N, M = map(int, input().split())
    if N == 0:
        break
    S = []
    for _ in range(M):
        row = list(map(int, input().split()))
        S.append(row)
    ans = 0
    for i in range(N):
        col_sum = 0
        for j in range(M):
            col_sum += S[j][i]
        if col_sum > ans:
            ans = col_sum
    print(ans)
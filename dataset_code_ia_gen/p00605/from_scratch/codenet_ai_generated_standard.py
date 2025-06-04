while True:
    N, K = map(int, input().split())
    if N == 0 and K == 0:
        break
    S = list(map(int, input().split()))
    B = [list(map(int, input().split())) for _ in range(N)]
    total_needed = [0]*K
    for i in range(N):
        for j in range(K):
            total_needed[j] += B[i][j]
    print("Yes" if all(total_needed[j] <= S[j] for j in range(K)) else "No")
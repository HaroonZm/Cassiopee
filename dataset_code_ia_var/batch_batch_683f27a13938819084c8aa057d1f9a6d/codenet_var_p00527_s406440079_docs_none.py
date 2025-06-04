def main():
    M, N = map(int, input().split())
    S = input()
    T = input()
    INF = 10**18
    dp0 = [[0]*(N+1) for _ in range(M+1)]
    dp1 = [[-INF]*(N+1) for _ in range(M+1)]
    for p in range(M+1):
        for q in range(N+1):
            v0 = dp0[p][q]
            v1 = dp1[p][q]
            if p < M:
                if S[p] == 'I':
                    dp1[p+1][q] = max(dp1[p+1][q], v0+1)
                else:
                    dp0[p+1][q] = max(dp0[p+1][q], v1+1)
            if q < N:
                if T[q] == 'I':
                    dp1[p][q+1] = max(dp1[p][q+1], v0+1)
                else:
                    dp0[p][q+1] = max(dp0[p][q+1], v1+1)
    ans = max(max(e) for e in dp1)
    print(max(ans, 0))
main()
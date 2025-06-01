def main():
    M, N = map(int, input().split())
    S, T = input(), input()

    INF = 10**18
    from itertools import product

    dp0 = [[0]*(N+1) for _ in range(M+1)]
    dp1 = [[-INF]*(N+1) for _ in range(M+1)]

    for p, q in product(range(M+1), range(N+1)):
        v0, v1 = dp0[p][q], dp1[p][q]

        if p < M:
            char_s = S[p]
            if char_s == 'I':
                dp1[p+1][q] = max(dp1[p+1][q], v0 + 1)
            else:
                dp0[p+1][q] = max(dp0[p+1][q], v1 + 1)
        if q < N:
            char_t = T[q]
            if char_t == 'I':
                dp1[p][q+1] = max(dp1[p][q+1], v0 + 1)
            else:
                dp0[p][q+1] = max(dp0[p][q+1], v1 + 1)

    print(max(max(row) for row in dp1 + [[0]]))

main()
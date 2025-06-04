N, M = map(int, input().split())
A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]
ans = 'No'
for i in range(N - M + 1):
    for j in range(N - M + 1):
        ok = True
        for k in range(M):
            for l in range(M):
                if A[i + k][j + l] != B[k][l]:
                    ok = False
        if ok:
            ans = 'Yes'
print(ans)
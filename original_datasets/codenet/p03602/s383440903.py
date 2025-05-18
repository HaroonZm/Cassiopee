N = int(input())
A = [[] for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    A[i] = line

for k in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][j] > A[i][k] + A[k][j]:  # 最短でない
                print('-1')
                exit()

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(N):
            if k == i or k == j:
                continue
            if A[i][j] == A[i][k] + A[k][j]:  # 代替可能
                break
        else:
            ans += A[i][j]

print(ans)
N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]

count = 0
for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            count += 1

print(count)
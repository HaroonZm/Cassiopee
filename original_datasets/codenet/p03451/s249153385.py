N = int(input())
A = [[0]*N for _ in range(2)]

A[0] = list(map(int, input().split()))
A[1] = list(map(int, input().split()))

ans = 0
for i in range(N):
    temp = 0
    for j in range(i+1):
        temp += A[0][j]
    for j in range(N-i):
        temp += A[1][-(j+1)]
    ans = max(ans, temp)

print(ans)
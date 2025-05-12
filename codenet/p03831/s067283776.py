N, A, B = map(int, input().split())
X = list(map(int, input().split()))

ans = 0

for i in range(1, N):
    dist = X[i] - X[i-1]
    if A*dist > B:
        ans += B
    else:
        ans += A*dist

print(ans)
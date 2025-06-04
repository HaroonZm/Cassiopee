n, k = map(int, input().split())

A = [-1] * n

for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in range(d):
        x = a[j] - 1
        if A[x] == -1:
            A[x] = 1

ans = 0

for i in range(n):
    if A[i] == -1:
        ans += 1

print(ans)
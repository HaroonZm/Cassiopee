N = int(input())
D, X = map(int, input().split())
A = []
for i in range(N):
    A.append(int(input()))

ans = X

for i in range(N):
    days = 1
    cnt = 0
    while days <= D:
        ans += 1
        cnt += 1
        days = cnt * A[i] + 1

print(ans)
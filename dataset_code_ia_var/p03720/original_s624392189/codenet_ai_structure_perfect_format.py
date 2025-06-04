n, m = map(int, input().split())
ans = [0] * n

for i in range(m):
    a, b = map(int, input().split())
    ans[a - 1] += 1
    ans[b - 1] += 1

for j in range(n):
    print(ans[j])
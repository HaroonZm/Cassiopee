n, m = map(int, input().split())
ans = 0
for i in range(n):
    a = list(map(int, input().split()))
    ans = max(ans, sum(a))
print(ans)
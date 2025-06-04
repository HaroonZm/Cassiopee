n = int(input())
a = list(map(int, input().split()))
ans = float("inf")
s = 0
for i in range(n):
    s += a[i]
    ans = min(ans, int(s / (i + 1)))
print(ans)
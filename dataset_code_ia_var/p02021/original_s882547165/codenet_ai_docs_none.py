n = int(input())
a = list(map(int, input().split()))
ans = 10 ** 7
s = 0
for i in range(n):
    s += a[i]
    ans = min(ans, s // (i + 1))
print(ans)
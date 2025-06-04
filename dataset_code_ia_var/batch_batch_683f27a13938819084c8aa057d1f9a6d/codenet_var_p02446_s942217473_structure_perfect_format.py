n = int(input())
a = list(map(int, input().split()))
a.append(20000000000)
ans = []
for i in range(n - 1, -1, -1):
    if a[i] != a[i - 1]:
        ans.append(a[i])
print(*reversed(ans))
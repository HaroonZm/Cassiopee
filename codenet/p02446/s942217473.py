n = int(input())
a = list(map(int, input().split( )))
a.append(20000000000)
ans = []
for i in range(0, n)[::-1]:
    if a[i] != a[i-1]:
        ans.append(a[i])
print(*reversed(ans))
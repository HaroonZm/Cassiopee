n = int(input())
a = list(map(int, input().split()))
d = []
l = 0
ans = 0
for i in range(n - 1):
    if a[i + 1] == a[i]:
        r = i + 1
        d.append(r - l)
        l = r
d.append(n - l)
if len(d) == 1:
    ans = d[0]
elif len(d) == 2:
    ans = max(d[0] + d[1], ans)
else:
    for i in range(len(d) - 2):
        ans = max(ans, d[i] + d[i + 1] + d[i + 2])
print(ans)
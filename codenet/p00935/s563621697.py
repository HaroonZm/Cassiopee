n, *d = map(int, open(0).read().split())
d = ''.join(map(str, d))
se = set()
for i in range(n):
    for j in range(i + 1, n + 1):
        se.add(int(d[i:j]))
ans = 0
while ans in se:
    ans += 1
print(ans)
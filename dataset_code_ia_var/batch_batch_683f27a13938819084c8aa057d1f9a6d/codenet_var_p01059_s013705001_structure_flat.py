n, m = map(int, input().split())
li = list(map(int, input().split()))
a = li[0] - 1
b = n - li[-1]
c = []
i = 1
while i < m:
    c.append((li[i]-li[i-1])//2)
    i += 1
res = [a, b]
for v in c:
    res.append(v)
print(max(res))
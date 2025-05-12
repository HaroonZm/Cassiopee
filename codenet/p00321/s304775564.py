n, f = map(int, input().split())
a = {}
for _ in range(n):
    m, *c = input().split()
    m = int(m)
    for i in range(m - 1):
        for j in range(i + 1, m):
            p = (min(c[i], c[j]), max(c[i], c[j]))
            if p in a:a[p] += 1
            else:a[p] = 1
b = []
for k in a:
    if a[k] >= f:b.append((k,a[k]))
b.sort(key = lambda x:x[0][1])
b.sort(key = lambda x:x[0][0])
print(len(b))
for i in b:print(*i[0])
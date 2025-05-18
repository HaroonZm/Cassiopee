n, *d = map(int, open(0).read().split())
d.sort()

a = [24 - b if i & 1 else b for i, b in enumerate(d)]
a.append(0)

ans = 24
print(min([abs(a[i] - a[j]) for i in range(n + 1)
           for j in range(i + 1, n + 1)]))
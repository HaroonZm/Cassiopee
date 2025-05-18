import bisect
m, n = map(int, input().split())
w = [tuple(map(int, input().split())) for _ in range(m)]
w, t = map(list,zip(*w))
for i in range(1, m):
    w[i] += w[i - 1]
    t[i] += t[i - 1]
c = [tuple(map(int, input().split())) for _ in range(n)]
c, b = map(list,zip(*c))
a = {}
a[tuple(range(n))] = -1
for _ in range(n):
    an = [(k,a[k]) for k in a]
    a = {}
    for x in an:
        for p in x[0]:
            if x[1] != -1:i = min(bisect.bisect_right(w, c[p] + w[x[1]], x[1]), bisect.bisect_right(t, b[p] + t[x[1]], x[1])) - 1
            else:i = min(bisect.bisect_right(w, c[p]), bisect.bisect_right(t, b[p])) - 1
            y = list(x[0])
            y.remove(p)
            y = tuple(y)
            if y in a:a[y] = max(a[y], i)
            else:a[y] = i
print(max([a[i] for i in a]) + 1)
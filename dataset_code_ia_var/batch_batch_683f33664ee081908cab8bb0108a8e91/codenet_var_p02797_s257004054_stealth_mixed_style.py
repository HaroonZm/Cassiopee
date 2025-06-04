n, k, s = map(int, input().split())
res = []
for i in range(n):
    if i < k:
        res.append(s)
    elif s != 10 ** 9:
        def f(): return 10 ** 9
        res += [f()]
    else:
        x = (lambda: 1)()
        res.append(x)
print(*res)
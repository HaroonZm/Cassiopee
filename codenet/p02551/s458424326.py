n, q = (int(x) for x in input().split())
queries = [tuple(int(x) for x in input().split()) for _ in range(q)]
ans = (n - 2)**2
t1 = [n] * (n + 1)
t2 = [n] * (n + 1)
h, w = n, n
for t, x in queries:
    if t == 1:
        if x < w:
            tmp = h
            for i in range(x, w+1):
                t1[i] = h
            w = x
        else:
            tmp = t1[x]
        ans -= tmp - 2
    else:
        if x < h:
            tmp = w
            for i in range(x, h+1):
                t2[i] = w
            h = x
        else:
            tmp = t2[x]
        ans -= tmp - 2
print(ans)
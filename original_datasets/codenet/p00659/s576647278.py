from itertools import combinations as C
while True:
    n = int(input())
    if n == 0: break
    d, dd, ddd = {}, {}, {}
    names = []
    for i in range(n):
        nmd = input().split()
        d[nmd[0]] = nmd[2:]
        names.append(nmd[0])
    for cc in list(C(d.items(), n-1)):
        t, tt = [], []
        for c in cc:
            t.append(c[0])
            tt += c[1]
        for name in names:
            if name not in t:
                dd[name] = tt
                break
    for k in d.keys():
        tmp = 0
        for v in d[k]:
            tmp += n-dd[k].count(v)
        ddd[k] = tmp
    ans = sorted(ddd.items(), key=lambda x: (x[1], x[0]))[0]
    print(ans[1], ans[0])
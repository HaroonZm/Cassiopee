from itertools import product
ci = "({["
co = ")}]"
while 1:
    p, q = map(int, input().split())
    if p == q == 0:
        break
    S = [input() for i in range(p)]
    T = [input() for i in range(q)]
    L = [set() for i in range(q)]

    for lens in product(range(1, 21), repeat=3):
        cnts = [0]*3
        ok = 1
        for s in S:
            idx = 0
            while s[idx] == '.':
                idx += 1
            if sum(c*l for c, l in zip(cnts, lens)) != idx:
                ok = 0
                break
            for c in s:
                if c in ci:
                    cnts[ci.index(c)] += 1
                elif c in co:
                    cnts[co.index(c)] -= 1
        if not ok:
            continue
        cnts = [0]*3
        for i, t in enumerate(T):
            idx = 0
            while t[idx] == '.':
                idx += 1
            L[i].add(sum(c*l for c, l in zip(cnts, lens)))
            for c in t:
                if c in ci:
                    cnts[ci.index(c)] += 1
                elif c in co:
                    cnts[co.index(c)] -= 1
    ans = [0]*q
    for i in range(q):
        if 1 < len(L[i]):
            ans[i] = -1
        else:
            v, = L[i]
            ans[i] = v
    print(*ans)
H, W = map(int, input().split())
ans = 0

C = [input() for _ in range(H)]
for i in range(2):
    L = [0]*H
    R = [0]*H
    Lk = []
    Rk = []
    for h in range(H):
        row = C[h]
        l = row.find("B")
        r = row.rfind("B")
        L[h] = l
        R[h] = r
        if l >= 0:
            Lk.append(h)
        if r >= 0:
            Rk.append(h)
    for lh in Lk:
        for rh in Rk:
            diff = abs(L[lh]-R[rh]) + abs(lh - rh)
            if diff > ans:
                ans = diff
    if i == 0:
        C2 = []
        for x in range(W):
            s = ""
            for y in range(H):
                s += C[y][x]
            C2.append(s)
        C = C2
        tmp = H
        H = W
        W = tmp
print(ans)
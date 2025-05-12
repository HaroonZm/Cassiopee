def inpl(): return list(map(int, input().split()))

H, W = inpl()
ans = 0

C = [input() for _ in range(H)]
for i in range(2):
    L = [0]*H
    R = [0]*H
    Lk = []
    Rk = []
    for h in range(H):
        L[h] = C[h].find("B")
        R[h] = C[h].rfind("B")
        if L[h] >= 0:
            Lk.append(h)
        if R[h] >= 0:
            Rk.append(h)
    
    for lh in Lk:
        for rh in Rk:
            ans = max(ans, abs(L[lh] - R[rh]) + abs(lh - rh))

    if i == 0:
        C = ["".join(c) for c in zip(*C)]
        H, W = W, H

print(ans)
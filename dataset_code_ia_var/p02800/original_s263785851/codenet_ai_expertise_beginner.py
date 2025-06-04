import sys
input = sys.stdin.readline

H, W = map(int, input().split())
A = []
for i in range(H):
    A.append(input().strip())

mod = 998244353

# Calcul des factorielles et inverses modulo mod
FACT = [1]
for i in range(1, 21):
    FACT.append((FACT[-1] * i) % mod)

FACT_INV = [pow(FACT[-1], mod - 2, mod)]
for i in range(20, 0, -1):
    FACT_INV.append((FACT_INV[-1] * i) % mod)
FACT_INV = FACT_INV[::-1]

# Tableau pour les combinaisons
COMBI = []
for i in range(21):
    COMBI.append([-1] * 21)

def Combi(a, b):
    if COMBI[a][b] != -1:
        return COMBI[a][b]
    if 0 <= b <= a:
        COMBI[a][b] = FACT[a] * FACT_INV[b] * FACT_INV[a-b] % mod
        return COMBI[a][b]
    else:
        COMBI[a][b] = 0
        return 0

M = max(H, W) + 1
RA = []
for i in range(M):
    RA.append([-1] * M)

def rect(HH, WW):
    if HH == 0 and WW == 0:
        return 1
    if RA[HH][WW] != -1:
        return RA[HH][WW]
    DP = []
    for i in range(HH+1):
        line = []
        for j in range(WW+1):
            line.append([0, 0])
        DP.append(line)
    DP[0][0][0] = 1
    DP[0][0][1] = 1

    for h in range(HH+1):
        for w in range(WW+1):
            # Vertical
            for nexth in range(h+1, HH+1):
                DP[nexth][w][0] += DP[h][w][1] * FACT_INV[nexth-h]
                DP[nexth][w][0] %= mod
            # Horizontal
            for nextw in range(w+1, WW+1):
                DP[h][nextw][1] += DP[h][w][0] * FACT_INV[nextw-w]
                DP[h][nextw][1] %= mod

    RA[HH][WW] = (DP[HH][WW][0] + DP[HH][WW][1]) % mod * FACT[HH] % mod * FACT[WW] % mod
    RA[WW][HH] = RA[HH][WW]
    return RA[HH][WW]

CA = []
for i in range(H+1):
    CA.append([-1] * (W+1))

def calc(h, w):
    if CA[h][w] != -1:
        return CA[h][w]
    RET = 0
    for bh in range(h+1):
        for bw in range(w+1):
            v = rect(bh, w-bw) * rect(h-bh, bw) * Combi(h,bh) * Combi(w,bw)
            RET += v
            RET %= mod
    CA[h][w] = RET % mod
    return CA[h][w]

for i in range(H+1):
    for j in range(W+1):
        calc(i, j)

ANS = rect(H, W)

for i in range((1 << H) - 1):
    for j in range((1 << W) - 1):
        okflag = 1
        for h in range(H):
            if (i & (1 << h)) != 0:
                continue
            coinc = ""
            dif = 0
            for w in range(W):
                if (j & (1 << w)) != 0:
                    continue
                if coinc == "":
                    coinc = A[h][w]
                elif A[h][w] != coinc:
                    dif = 1
                    break
            if dif == 0:
                okflag = 0
                break
        if okflag == 0:
            continue

        okflag = 1
        for w in range(W):
            if (j & (1 << w)) != 0:
                continue
            coinc = ""
            dif = 0
            for h in range(H):
                if (i & (1 << h)) != 0:
                    continue
                if coinc == "":
                    coinc = A[h][w]
                elif A[h][w] != coinc:
                    dif = 1
                    break
            if dif == 0:
                okflag = 0
                break
        if okflag == 0:
            continue

        HR = 0
        for h in range(H):
            if (i & (1 << h)) != 0:
                HR += 1
        WR = 0
        for w in range(W):
            if (j & (1 << w)) != 0:
                WR += 1
        ANS += CA[HR][WR]
        # ANS %= mod

print(ANS % mod)
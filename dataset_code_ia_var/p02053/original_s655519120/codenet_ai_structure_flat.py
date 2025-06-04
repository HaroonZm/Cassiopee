H, W = map(int, input().split())
MAP = []
i = 0
while i < H:
    MAP.append(list(input()))
    i += 1

BLIST = []
i = 0
while i < H:
    j = 0
    while j < W:
        if MAP[i][j] == "B":
            BLIST.append([i, j])
        j += 1
    i += 1

n = len(BLIST)
idx_min = 0
idx_max = 0
minv = BLIST[0][0] + BLIST[0][1]
maxv = BLIST[0][0] + BLIST[0][1]
k = 1
while k < n:
    s = BLIST[k][0] + BLIST[k][1]
    if s < minv:
        minv = s
        idx_min = k
    if s > maxv:
        maxv = s
        idx_max = k
    k += 1
ANS = abs(BLIST[idx_min][0] - BLIST[idx_max][0]) + abs(BLIST[idx_min][1] - BLIST[idx_max][1])

idx_min = 0
idx_max = 0
minv = BLIST[0][0] - BLIST[0][1]
maxv = BLIST[0][0] - BLIST[0][1]
k = 1
while k < n:
    s = BLIST[k][0] - BLIST[k][1]
    if s < minv:
        minv = s
        idx_min = k
    if s > maxv:
        maxv = s
        idx_max = k
    k += 1
tmp = abs(BLIST[idx_min][0] - BLIST[idx_max][0]) + abs(BLIST[idx_min][1] - BLIST[idx_max][1])
if tmp > ANS:
    ANS = tmp

print(ANS)
n, k = map(int, input().split())
plst = [tuple(map(int, input().split())) for _ in range(n)]

xlst = sorted({x for p in plst for x in (p[0], p[3])})
ylst = sorted({y for p in plst for y in (p[1], p[4])})
dlst = sorted({d for p in plst for d in (p[2], p[5])})

xdic = {v: i for i, v in enumerate(xlst)}
ydic = {v: i for i, v in enumerate(ylst)}
ddic = {v: i for i, v in enumerate(dlst)}

lx, ly, ld = len(xlst), len(ylst), len(dlst)
new_map = [[[0]*ld for _ in range(ly)] for __ in range(lx)]

for x1, y1, d1, x2, y2, d2 in plst:
    x1, y1, d1, x2, y2, d2 = xdic[x1], ydic[y1], ddic[d1], xdic[x2], ydic[y2], ddic[d2]
    for x in range(x1, x2):
        for y in range(y1, y2):
            for d in range(d1, d2):
                new_map[x][y][d] += 1

ans = sum(
    (xlst[i+1]-xlst[i])*(ylst[j+1]-ylst[j])*(dlst[z+1]-dlst[z])
    for i in range(lx-1)
    for j in range(ly-1)
    for z in range(ld-1)
    if new_map[i][j][z] >= k
)
print(ans)
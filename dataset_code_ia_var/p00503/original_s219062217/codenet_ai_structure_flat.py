n, k = map(int, input().split())

plst = []
xlst = []
ylst = []
dlst = []

for _ in range(n):
    x1, y1, d1, x2, y2, d2 = map(int, input().split())
    plst.append((x1, y1, d1, x2, y2, d2))
    xlst.append(x1)
    xlst.append(x2)
    ylst.append(y1)
    ylst.append(y2)
    dlst.append(d1)
    dlst.append(d2)

xlst = list(set(xlst))
ylst = list(set(ylst))
dlst = list(set(dlst))

xlst.sort()
ylst.sort()
dlst.sort()

xdic = {}
ydic = {}
ddic = {}

i = 0
for v in xlst:
    xdic[v] = i
    i += 1
i = 0
for v in ylst:
    ydic[v] = i
    i += 1
i = 0
for v in dlst:
    ddic[v] = i
    i += 1

dimx = len(xlst)
dimy = len(ylst)
dimd = len(dlst)
new_map = []
i = 0
while i < dimx:
    temp2 = []
    j = 0
    while j < dimy:
        temp2.append([0]*dimd)
        j += 1
    new_map.append(temp2)
    i += 1

for idx in range(len(plst)):
    p = plst[idx]
    x1 = xdic[p[0]]
    y1 = ydic[p[1]]
    d1 = ddic[p[2]]
    x2 = xdic[p[3]]
    y2 = ydic[p[4]]
    d2 = ddic[p[5]]
    x = x1
    while x < x2:
        y = y1
        while y < y2:
            d = d1
            while d < d2:
                new_map[x][y][d] += 1
                d += 1
            y += 1
        x += 1

ans = 0
i = 0
while i < len(xlst)-1:
    xlsti = xlst[i]
    xlsti1 = xlst[i+1]
    x = xdic[xlsti]
    j = 0
    while j < len(ylst)-1:
        ylstj = ylst[j]
        ylstj1 = ylst[j+1]
        y = ydic[ylstj]
        z = 0
        while z < len(dlst)-1:
            dlstz = dlst[z]
            dlstz1 = dlst[z+1]
            d = ddic[dlstz]
            if new_map[x][y][d] >= k:
                ans += (xlsti1 - xlsti) * (ylstj1 - ylstj) * (dlstz1 - dlstz)
            z += 1
        j += 1
    i += 1
print(ans)
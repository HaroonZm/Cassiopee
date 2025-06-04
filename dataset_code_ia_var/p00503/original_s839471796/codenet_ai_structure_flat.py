n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])
plst = []
xlst = []
ylst = []
dlst = []
i = 0
while i < n:
    values = list(map(int, input().split()))
    x1 = values[0]
    y1 = values[1]
    d1 = values[2]
    x2 = values[3]
    y2 = values[4]
    d2 = values[5]
    plst.append((x1, y1, d1, x2, y2, d2))
    xlst.append(x1)
    xlst.append(x2)
    ylst.append(y1)
    ylst.append(y2)
    dlst.append(d1)
    dlst.append(d2)
    i += 1

uniq_x = {}
uniq_y = {}
uniq_d = {}
tmp = []
for v in xlst:
    if v not in uniq_x:
        uniq_x[v] = 1
        tmp.append(v)
xlst = tmp
xlst.sort()
tmp = []
for v in ylst:
    if v not in uniq_y:
        uniq_y[v] = 1
        tmp.append(v)
ylst = tmp
ylst.sort()
tmp = []
for v in dlst:
    if v not in uniq_d:
        uniq_d[v] = 1
        tmp.append(v)
dlst = tmp
dlst.sort()

xdic = {}
ydic = {}
ddic = {}
i = 0
while i < len(xlst):
    xdic[xlst[i]] = i
    i += 1
i = 0
while i < len(ylst):
    ydic[ylst[i]] = i
    i += 1
i = 0
while i < len(dlst):
    ddic[dlst[i]] = i
    i += 1

new_map = []
i = 0
while i < len(xlst):
    inner_lst = []
    j = 0
    while j < len(ylst):
        inner_lst.append([0] * len(dlst))
        j += 1
    new_map.append(inner_lst)
    i += 1

i = 0
while i < len(plst):
    p = plst[i]
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
    i += 1

ans = 0
i = 0
while i < len(xlst) - 1:
    j = 0
    while j < len(ylst) - 1:
        z = 0
        while z < len(dlst) - 1:
            x = xdic[xlst[i]]
            y = ydic[ylst[j]]
            d = ddic[dlst[z]]
            if new_map[x][y][d] >= k:
                ans += (xlst[i + 1] - xlst[i]) * (ylst[j + 1] - ylst[j]) * (dlst[z + 1] - dlst[z])
            z += 1
        j += 1
    i += 1
print(ans)
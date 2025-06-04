n_k = input().split()
n = int(n_k[0])
k = int(n_k[1])
plst = []
xlst = []
ylst = []
dlst = []
for _ in range(n):
    l = input().split()
    x1 = int(l[0])
    y1 = int(l[1])
    d1 = int(l[2])
    x2 = int(l[3])
    y2 = int(l[4])
    d2 = int(l[5])
    plst.append((x1, y1, d1, x2, y2, d2))
    xlst.append(x1)
    xlst.append(x2)
    ylst.append(y1)
    ylst.append(y2)
    dlst.append(d1)
    dlst.append(d2)
s1 = set()
for v in xlst:
    s1.add(v)
xlst = list(s1)
s2 = set()
for v in ylst:
    s2.add(v)
ylst = list(s2)
s3 = set()
for v in dlst:
    s3.add(v)
dlst = list(s3)
xlst.sort()
ylst.sort()
dlst.sort()
lx = len(xlst)
ly = len(ylst)
ld = len(dlst)
xdic = {}
for i in range(lx):
    xdic[xlst[i]] = i
ydic = {}
for i in range(ly):
    ydic[ylst[i]] = i
ddic = {}
for i in range(ld):
    ddic[dlst[i]] = i
new_map = []
for i in range(lx):
    temp = []
    for j in range(ly):
        tmp2 = []
        for l in range(ld):
            tmp2.append(0)
        temp.append(tmp2)
    new_map.append(temp)
for idx in range(len(plst)):
    t = plst[idx]
    x1 = xdic[t[0]]
    y1 = ydic[t[1]]
    d1 = ddic[t[2]]
    x2 = xdic[t[3]]
    y2 = ydic[t[4]]
    d2 = ddic[t[5]]
    for x in range(x1, x2):
        for y in range(y1, y2):
            for d in range(d1, d2):
                new_map[x][y][d] += 1
ans = 0
i = 0
while i < lx - 1:
    xlsti = xlst[i]
    xlsti1 = xlst[i+1]
    x = xdic[xlsti]
    j = 0
    while j < ly - 1:
        ylstj = ylst[j]
        ylstj1 = ylst[j+1]
        y = ydic[ylstj]
        z = 0
        while z < ld - 1:
            dlstz = dlst[z]
            dlstz1 = dlst[z+1]
            d = ddic[dlstz]
            if new_map[x][y][d] >= k:
                ans += (xlsti1 - xlsti) * (ylstj1 - ylstj) * (dlstz1 - dlstz)
            z += 1
        j += 1
    i += 1
print(ans)
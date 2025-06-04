s = input()
gx, gy = map(int, input().split())
lists = list(s.split("T"))
xlist = []
ylist = []
if s[0] == "T":
    for i in range(len(lists)):
        if i % 2 == 0:
            xlist.append(len(lists[i]))
        else:
            ylist.append(len(lists[i]))
elif s[0] == "F":
    for i in range(len(lists)):
        if i % 2 == 0:
            xlist.append(len(lists[i]))
        else:
            ylist.append(len(lists[i]))
    gx -= xlist[0]
    del xlist[0]
Xsum = sum(xlist)
Ysum = sum(ylist)
if (Xsum + gx) % 2 != 0 or (Ysum + gy) % 2 != 0:
    print("No")
else:
    gx1 = (Xsum + gx) // 2
    gx2 = (Xsum - gx) // 2
    gy1 = (Ysum + gy) // 2
    gy2 = (Ysum - gy) // 2
    dpx = [[False for i in range(Xsum + 2)] for j in range(len(xlist) + 2)]
    dpy = [[False for i in range(Ysum + 2)] for j in range(len(ylist) + 2)]
    dpx[0][0] = True
    dpy[0][0] = True
    for i in range(len(xlist)):
        for j in range(Xsum + 2):
            if j - xlist[i] >= 0:
                dpx[i + 1][j] = dpx[i][j - xlist[i]] or dpx[i][j]
            else:
                dpx[i + 1][j] = dpx[i][j]
    for i in range(len(ylist)):
        for j in range(Ysum + 2):
            if j - ylist[i] >= 0:
                dpy[i + 1][j] = dpy[i][j - ylist[i]] or dpy[i][j]
            else:
                dpy[i + 1][j] = dpy[i][j]
    flag1 = False
    if 0 <= gy1 <= Ysum:
        if dpy[len(ylist)][gy1]:
            flag1 = True
    flag2 = False
    if 0 <= gy2 <= Ysum:
        if dpy[len(ylist)][gy2]:
            flag2 = True
    flag3 = False
    if 0 <= gx1 <= Xsum:
        if dpx[len(xlist)][gx1]:
            flag3 = True
    flag4 = False
    if 0 <= gx2 <= Xsum:
        if dpx[len(xlist)][gx2]:
            flag4 = True
    if (flag1 or flag2) and (flag3 or flag4):
        print("Yes")
    else:
        print("No")
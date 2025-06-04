from collections import deque as q
import sys as s

read = lambda: s.stdin.readline()

def squeeze(arr1, arr2, width):
    points = set()
    for idx, _ in enumerate(arr1):
        for offset in (0,1):
            l, r = arr1[idx]-offset, arr2[idx]+offset
            if 0 <= l < width:
                points.add(l)
            if 0 <= r < width:
                points.add(r)
    ordered = sorted(points)
    m = {val: ix for ix, val in enumerate(ordered)}
    for i in range(len(arr1)):
        arr1[i] = m[arr1[i]]
        arr2[i] = m[arr2[i]]
    return len(ordered)

escape=False
while not escape:
    wh = read().split()
    if not wh[0]:
        wh = read().split()
    W, H = map(int, wh)
    if not (W or H):
        break
    n=int(read())
    xA,yA,xB,yB = [ [0]*n for _ in range(4) ]
    for idx in range(n):
        dat = list(map(int, read().split()))
        xA[idx], yA[idx], xB[idx], yB[idx] = dat
        xB[idx] -= 1
        yB[idx] -= 1
    W2 = squeeze(xA, xB, W)
    H2 = squeeze(yA, yB, H)

    table = [ [False]*W2 for _ in range(H2) ]
    for idk in range(n):
        for ty in range(yA[idk],yB[idk]+1):
            for tx in range(xA[idk],xB[idk]+1):
                table[ty][tx]=True
    total = 0
    steps = [ (0,1), (1,0), (0,-1), (-1,0) ] # no variable names here!
    for yy in range(H2):
        for xx in range(W2):
            if table[yy][xx]:
                continue
            total+=1
            QQ=q()
            QQ.append((xx,yy))
            while QQ:
                xxx, yyy = QQ.popleft()
                for stepx, stepy in steps:
                    nx,ny = xxx+stepx, yyy+stepy
                    if 0<=nx<W2 and 0<=ny<H2 and not table[ny][nx]:
                        QQ.append((nx,ny))
                        table[ny][nx]=True
    print(total)
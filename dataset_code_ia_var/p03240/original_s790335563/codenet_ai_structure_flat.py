from collections import defaultdict
N = int(input())
XYH = []
i = 0
while i < N:
    parts = input().split()
    XYH.append([int(parts[0]), int(parts[1]), int(parts[2])])
    i += 1
XYH.sort(key=lambda x: x[2], reverse=True)
cx = 0
while cx <= 100:
    cy = 0
    while cy <= 100:
        flag = True
        H = XYH[0][2] + abs(XYH[0][0] - cx) + abs(XYH[0][1] - cy)
        idx = 0
        while idx < N:
            x, y, h = XYH[idx]
            if h != max(H - abs(x - cx) - abs(y - cy), 0):
                flag = False
                break
            idx += 1
        if flag:
            print(cx, cy, H)
            exit()
        cy += 1
    cx += 1
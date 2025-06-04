s = input()
gx_gy = input().split()
gx = int(gx_gy[0])
gy = int(gx_gy[1])
parts = s.split("T")
x_moves = []
y_moves = []
if s[0] == "T":
    for i in range(len(parts)):
        if i % 2 == 0:
            x_moves.append(len(parts[i]))
        else:
            y_moves.append(len(parts[i]))
else:
    for i in range(len(parts)):
        if i % 2 == 0:
            x_moves.append(len(parts[i]))
        else:
            y_moves.append(len(parts[i]))
    gx = gx - x_moves[0]
    x_moves.pop(0)
sum_x = sum(x_moves)
sum_y = sum(y_moves)
if (sum_x + gx) % 2 != 0 or (sum_y + gy) % 2 != 0:
    print("No")
else:
    gx1 = (sum_x + gx) // 2
    gx2 = (sum_x - gx) // 2
    gy1 = (sum_y + gy) // 2
    gy2 = (sum_y - gy) // 2
    dpx = []
    for i in range(len(x_moves) + 2):
        dpx.append([False] * (sum_x + 2))
    dpy = []
    for i in range(len(y_moves) + 2):
        dpy.append([False] * (sum_y + 2))
    dpx[0][0] = True
    dpy[0][0] = True
    for i in range(len(x_moves)):
        for j in range(sum_x + 2):
            if j - x_moves[i] >= 0 and dpx[i][j - x_moves[i]]:
                dpx[i + 1][j] = True
            if dpx[i][j]:
                dpx[i + 1][j] = True
    for i in range(len(y_moves)):
        for j in range(sum_y + 2):
            if j - y_moves[i] >= 0 and dpy[i][j - y_moves[i]]:
                dpy[i + 1][j] = True
            if dpy[i][j]:
                dpy[i + 1][j] = True
    x_ok1 = False
    if gx1 >= 0 and gx1 <= sum_x:
        if dpx[len(x_moves)][gx1]:
            x_ok1 = True
    x_ok2 = False
    if gx2 >= 0 and gx2 <= sum_x:
        if dpx[len(x_moves)][gx2]:
            x_ok2 = True
    y_ok1 = False
    if gy1 >= 0 and gy1 <= sum_y:
        if dpy[len(y_moves)][gy1]:
            y_ok1 = True
    y_ok2 = False
    if gy2 >= 0 and gy2 <= sum_y:
        if dpy[len(y_moves)][gy2]:
            y_ok2 = True
    if (x_ok1 or x_ok2) and (y_ok1 or y_ok2):
        print("Yes")
    else:
        print("No")
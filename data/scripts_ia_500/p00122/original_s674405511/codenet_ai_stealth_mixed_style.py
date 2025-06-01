dX = [2, 2, 2, 1, 0, -1, -2, -2, -2, -1, 0, 1]
dY = [-1, 0, 1, 2, 2, 2, 1, 0, -1, -2, -2, -2]

def doa(x, y, sx, sy):
    if x < 0 or x > 9 or y < 0 or y > 9:
        return False
    return abs(x - sx) < 2 and abs(y - sy) < 2

def solve(x, y, i):
    if i == 2 * n:
        return True
    sx, sy = xy[i], xy[i + 1]
    for idx in range(len(dX)):
        dx, dy = dX[idx], dY[idx]
        if doa(x + dx, y + dy, sx, sy):
            if solve(x + dx, y + dy, i + 2):
                return True
    return False

while True:
    line = raw_input()
    if line == "":
        continue
    x_str, y_str = line.split()
    x, y = int(x_str), int(y_str)
    if x == 0 and y == 0:
        break
    n = int(raw_input())
    xy = [int(k) for k in raw_input().split()]
    print("OK" if solve(x, y, 0) else "NA")
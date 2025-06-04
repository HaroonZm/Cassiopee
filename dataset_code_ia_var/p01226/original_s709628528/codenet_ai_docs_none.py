def move(y, x):
    p[2], p[3] = y, x
    if a[p[0] + y][p[1] + x] == ".":p[0] += y;p[1] += x

def shoot():
    th = p[0] + p[2]
    tw = p[1] + p[3]
    while 1:
        if a[th][tw] == "*":a[th][tw] = ".";break
        elif a[th][tw] == "#":break
        else: th += p[2]; tw += p[3]

for u in range(int(input())):
    if u > 0:print()
    h, w = map(int, input().split())
    a = [["#"] * (w + 2)] + [["#"] + list(input()) + ["#"] for _ in range(h)] + [["#"] * (w + 2)]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if a[i][j] == ">":p = [i, j, 0, 1];a[i][j] = ".";break
            elif a[i][j] == "^":p = [i, j, -1, 0];a[i][j] = ".";break
            elif a[i][j] == "<":p = [i, j, 0, -1];a[i][j] = ".";break
            elif a[i][j] == "v":p = [i, j, 1, 0];a[i][j] = ".";break
    n, c = int(input()), input()
    for i in range(n):
        if c[i] == "U":move(-1, 0)
        elif c[i] == "R":move(0, 1)
        elif c[i] == "L":move(0, -1)
        elif c[i] == "D":move(1, 0)
        else:shoot()
    if (p[2], p[3]) == (0, 1):a[p[0]][p[1]] = ">"
    elif (p[2], p[3]) == (-1, 0):a[p[0]][p[1]] = "^"
    elif (p[2], p[3]) == (0, -1):a[p[0]][p[1]] = "<"
    else:a[p[0]][p[1]] = "v"
    for i in a[1:-1]:print("".join(i[1:-1]))
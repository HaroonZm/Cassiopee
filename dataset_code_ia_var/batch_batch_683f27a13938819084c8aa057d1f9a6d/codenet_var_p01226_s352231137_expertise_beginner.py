dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
tanks = "<^>v"
flat = "."
brick = "*"
iron = "#"
water = "-"

case = int(raw_input())
for t in range(case):
    h, w = map(int, raw_input().split())
    m = []
    for i in range(h):
        m.append(list(raw_input()))
    n = int(raw_input())
    s = raw_input()
    x = 0
    y = 0
    d = 0
    for i in range(h):
        for j in range(w):
            if m[i][j] in tanks:
                x = j
                y = i
                d = tanks.index(m[i][j])
                m[i][j] = flat
    for comm in s:
        if comm == "U":
            d = 1
            if y > 0 and m[y-1][x] == flat:
                y = y - 1
        elif comm == "D":
            d = 3
            if y < h-1 and m[y+1][x] == flat:
                y = y + 1
        elif comm == "L":
            d = 0
            if x > 0 and m[y][x-1] == flat:
                x = x - 1
        elif comm == "R":
            d = 2
            if x < w-1 and m[y][x+1] == flat:
                x = x + 1
        else:
            nx = x + dx[d]
            ny = y + dy[d]
            while nx >= 0 and nx <= w-1 and ny >= 0 and ny <= h-1:
                obj = m[ny][nx]
                if obj == brick:
                    m[ny][nx] = flat
                    break
                elif obj == iron:
                    break
                nx = nx + dx[d]
                ny = ny + dy[d]
    m[y][x] = tanks[d]
    for i in range(h):
        print "".join(m[i])
    if t < case - 1:
        print
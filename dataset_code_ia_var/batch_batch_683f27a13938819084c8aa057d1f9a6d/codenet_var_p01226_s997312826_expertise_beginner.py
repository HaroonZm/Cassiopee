t = int(input())
for i in range(t):
    h, w = map(int, input().split())
    mp = []
    for _ in range(h):
        row = input()
        mp.append(["#"] + list(row) + ["#"])
    border = ["#"] * (w + 2)
    mp.insert(0, border)
    mp.append(border[:])

    for y in range(h + 2):
        for x in range(w + 2):
            if mp[y][x] == ">":
                sx = x
                sy = y
                sd = 0
            if mp[y][x] == "^":
                sx = x
                sy = y
                sd = 1
            if mp[y][x] == "<":
                sx = x
                sy = y
                sd = 2
            if mp[y][x] == "v":
                sx = x
                sy = y
                sd = 3

    mp[sy][sx] = "."

    n = int(input())
    s = input()

    vec = [(1,0), (0,-1), (-1,0), (0,1)]
    dic = {"R":0, "U":1, "L":2, "D":3}
    tank = {0:">", 1:"^", 2:"<", 3:"v"}

    for c in s:
        if c == "S":
            dx, dy = vec[sd]
            nx = sx
            ny = sy
            while True:
                nx += dx
                ny += dy
                if mp[ny][nx] == "#":
                    break
                if mp[ny][nx] == "*":
                    mp[ny][nx] = "."
                    break
        else:
            sd = dic[c]
            dx, dy = vec[sd]
            if mp[sy+dy][sx+dx] == ".":
                sx += dx
                sy += dy

    mp[sy][sx] = tank[sd]
    for j in range(1, h+1):
        row_str = ""
        for k in range(1, w+1):
            row_str += mp[j][k]
        print(row_str)
    if i != t-1:
        print()
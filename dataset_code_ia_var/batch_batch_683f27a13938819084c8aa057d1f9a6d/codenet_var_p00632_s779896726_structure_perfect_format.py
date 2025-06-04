from collections import deque

while True:
    h, w = map(int, input().split())
    if h == 0:
        break
    mp = [list("X" + input() + "X") for _ in range(h)]
    mp.insert(0, ["X"] * (w + 2))
    mp.append(["X"] * (w + 2))

    for y in range(h + 2):
        for x in range(w + 2):
            if mp[y][x] == "A":
                ax, ay = x, y
                mp[y][x] = "."
            if mp[y][x] == "B":
                bx, by = x, y
                mp[y][x] = "."
    INF = 1000
    dist_mp = [[INF] * (w + 2) for _ in range(h + 2)]
    dist_mp[ay][ax] = 0
    que = deque()
    que.append((0, ax, ay))
    vec = ((1, 0), (0, -1), (-1, 0), (0, 1))
    while que:
        d, x, y = que.popleft()
        for dx, dy in vec:
            nx, ny = x + dx, y + dy
            if mp[ny][nx] == "." and dist_mp[ny][nx] == INF:
                que.append((d + 1, nx, ny))
                dist_mp[ny][nx] = d + 1

    limit = d
    pattern = input()
    length = len(pattern)
    t = 0
    dic = {}
    while True:
        if t >= dist_mp[by][bx]:
            print(t, by - 1, bx - 1)
            break
        if t > limit:
            if (t % length, bx, by) in dic:
                print("impossible")
                break
            else:
                dic[(t % length, bx, by)] = True
        c = pattern[t % length]
        if c == "5":
            pass
        elif c == "8" and mp[by - 1][bx] != "X":
            by -= 1
        elif c == "6" and mp[by][bx + 1] != "X":
            bx += 1
        elif c == "4" and mp[by][bx - 1] != "X":
            bx -= 1
        elif c == "2" and mp[by + 1][bx] != "X":
            by += 1
        t += 1
    else:
        print("impossible")
t = int(input())
vec = ((1, 0), (0, -1), (-1, 0), (0, 1))
for _ in range(t):
    mp = [list("X" * 8)]
    for _ in range(12):
        mp.append(list("X" + input() + "X"))
    mp.append(list("X" * 8))
    cnt = 0
    while True:
        checked = [[None] * 8 for _ in range(14)]
        for y in range(1, 13):
            for x in range(1, 7):
                if mp[y][x] in ("O", ".", "X"):
                    checked[y][x] = False
        for y in range(1, 13):
            for x in range(1, 7):
                if mp[y][x] not in ("O", ".", "X") and checked[y][x] is None:
                    stack = [(x, y)]
                    color = mp[y][x]
                    lst = []
                    while stack:
                        cx, cy = stack.pop()
                        if checked[cy][cx] is not None:
                            continue
                        checked[cy][cx] = False
                        lst.append((cx, cy))
                        for dx, dy in vec:
                            nx, ny = cx + dx, cy + dy
                            if mp[ny][nx] == color and checked[ny][nx] is None:
                                stack.append((nx, ny))
                    if len(lst) >= 4:
                        for px, py in lst:
                            checked[py][px] = True
        any_remove = False
        for row in checked:
            for val in row:
                if val:
                    any_remove = True
        if not any_remove:
            break
        for y in range(1, 13):
            for x in range(1, 7):
                if mp[y][x] == "O":
                    for dx, dy in vec:
                        nx, ny = x + dx, y + dy
                        if mp[ny][nx] != "O" and checked[ny][nx]:
                            checked[y][x] = True
        for y in range(1, 13):
            for x in range(1, 7):
                if checked[y][x]:
                    mp[y][x] = "."
        for x in range(1, 7):
            s = ""
            for y in range(12, 0, -1):
                s = mp[y][x] + s
            s = s.replace(".", "")
            s = "." * (12 - len(s)) + s
            for y in range(12, 0, -1):
                mp[y][x] = s[y - 1]
        cnt += 1
    print(cnt)
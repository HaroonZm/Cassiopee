from collections import deque

while True:
    x, y = map(int, input().split())
    if x == 0:
        break
    mp = [list("#" * (x + 2))]
    for _ in range(y):
        mp.append(list("#" + input() + "#"))
    mp.append(list("#" * (x + 2)))
    ice_cnt = 0
    ice_dic = []
    vec = ((1, 0), (0, -1), (-1, 0), (0, 1))

    for i in range(1, y + 1):
        for j in range(1, x + 1):
            if mp[i][j] == "S":
                sx, sy = j, i
                mp[i][j] = "."
            if mp[i][j] == "G":
                gx, gy = j, i
                mp[i][j] = "."
    stack = []
    for i in range(1, y + 1):
        for j in range(1, x + 1):
            if mp[i][j] == "X":
                mp[i][j] = ice_cnt
                ice_dic.append(1)
                stack.append((j, i))
                while stack:
                    cx, cy = stack.pop()
                    for dx, dy in vec:
                        nx, ny = cx + dx, cy + dy
                        if mp[ny][nx] == "X":
                            mp[ny][nx] = ice_cnt
                            ice_dic[ice_cnt] += 1
                            stack.append((nx, ny))
                ice_cnt += 1

    que = deque()
    que.append((0, sx, sy, [v // 2 for v in ice_dic], 0))
    dic = {}
    dic[(sx, sy, 0)] = 0
    hash_lst = [150 ** i for i in range(len(ice_dic))]
    found = False
    while que and not found:
        score, px, py, counters, hs = que.popleft()
        if (px, py) == (gx, gy):
            print(score)
            found = True
            break
        for dx, dy in vec:
            nx, ny = px + dx, py + dy
            if mp[ny][nx] == "#":
                continue
            elif mp[ny][nx] == ".":
                if (nx, ny, hs) in dic:
                    continue
                dic[(nx, ny, hs)] = True
                que.append((score + 1, nx, ny, counters[:], hs))
            else:
                num = mp[ny][nx]
                if counters[num] <= 0:
                    continue
                new_counters = counters[:]
                new_counters[num] -= 1
                new_hs = hs + hash_lst[num]
                if (nx, ny, new_hs) in dic:
                    continue
                dic[(nx, ny, new_hs)] = True
                que.append((score + 1, nx, ny, new_counters, new_hs))
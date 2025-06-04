B = 13
M = 9
S = 5

dx = [0, 0, 1, 0, -1, 1, 1, -1, -1, 0, 2, 0, -2]
dy = [0, -1, 0, 1, 0, -1, 1, 1, -1, 2, 0, -2, 0]

def isOnCloth(x, y):
    return x >= 0 and x < 10 and y >= 0 and y < 10

def soak(cloth, x, y, ink):
    for i in range(ink):
        cloth[y + dy[i]][x + dx[i]] = cloth[y + dy[i]][x + dx[i]] - 1

def drop(cloth, x, y, ink):
    for i in range(ink):
        cloth[y + dy[i]][x + dx[i]] = cloth[y + dy[i]][x + dx[i]] + 1

def canSoak(cloth, x, y, ink):
    for i in range(ink):
        nx = x + dx[i]
        ny = y + dy[i]
        if not isOnCloth(nx, ny) or cloth[ny][nx] <= 0:
            return False
    return True

def DFS(cloth, ink_set, cur):
    if len(ink_set) == 0:
        return []
    while cur < 100:
        if cloth[cur // 10][cur % 10] != 0:
            break
        cur = cur + 1
    for ink in set(ink_set):
        for i in range(ink):
            cx = cur % 10 + dx[i]
            cy = cur // 10 + dy[i]
            if isOnCloth(cx, cy) and cloth[cy][cx] > 0:
                if canSoak(cloth, cx, cy, ink):
                    soak(cloth, cx, cy, ink)
                    ink_set.remove(ink)
                    result = DFS(cloth, ink_set, cur)
                    if result is not False:
                        result.append([cx, cy, ink])
                        return result
                    ink_set.append(ink)
                    drop(cloth, cx, cy, ink)
    return False

import itertools

n = int(input())
cloth = []
for u in range(10):
    row = input().split()
    row = [int(x) for x in row]
    cloth.append(row)

su = 0
for i in range(10):
    su = su + sum(cloth[i])

possible_inks = [0, 13, 9, 5]
ink_sets = []
for a in itertools.combinations_with_replacement(possible_inks, n):
    if sum(a) == su:
        ink_sets.append(list(a))

for ink_set in ink_sets:
    result = DFS(cloth, ink_set, 0)
    if result is not False:
        break

dic = {B: 3, M: 2, S: 1}

for r in result:
    print(str(r[0]) + " " + str(r[1]) + " " + str(dic[r[2]]))
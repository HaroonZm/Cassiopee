# Définir le dictionnaire qui sert à reconnaître les chiffres et opérateurs
dic = {
    ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)): "0",
    ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4)): "1",
    ((0, 0), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (1, 4), (2, 0), (2, 1), (2, 2), (2, 4)): "2",
    ((0, 0), (0, 2), (0, 4), (1, 0), (1, 2), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)): "3",
    ((0, 0), (0, 1), (0, 2), (1, 2), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)): "4",
    ((0, 0), (0, 1), (0, 2), (0, 4), (1, 0), (1, 2), (1, 4), (2, 0), (2, 2), (2, 3), (2, 4)): "5",
    ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (1, 4), (2, 0), (2, 2), (2, 3), (2, 4)): "6",
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)): "7",
    ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)): "8",
    ((0, 0), (0, 1), (0, 2), (0, 4), (1, 0), (1, 2), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4)): "9",
    ((0, 0), (1, -1), (1, 0), (1, 1), (2, 0)): "+",
    ((0, 0), (1, 0), (2, 0)): "-",
    ((0, 0),): "*"
}

n = int(input())
mp = []
for i in range(201):
    mp.append([0] * 201)

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2:  # Ligne verticale
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            mp[y][x1] = 1
    elif y1 == y2:  # Ligne horizontale
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            mp[y1][x] = 1

checked = []
for i in range(201):
    checked.append([False] * 201)

# Les directions pour explorer les voisins (bas, gauche, haut, droite)
vec = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def search(x, y, base_x, base_y, stack):
    for v in vec:
        dx = v[0]
        dy = v[1]
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= 201 or ny < 0 or ny >= 201:
            continue
        if mp[ny][nx] == 1 and checked[ny][nx] == False:
            checked[ny][nx] = True
            stack.append((nx-base_x, ny-base_y))
            search(nx, ny, base_x, base_y, stack)

res = ""
for x in range(201):
    for y in range(201):
        if mp[y][x] == 1 and checked[y][x] == False:
            checked[y][x] = True
            stack = [(0, 0)]
            search(x, y, x, y, stack)
            stack.sort()
            key = tuple(stack)
            res = res + dic[key]

print(eval(res))
import sys

# Lecture des données
NWH = raw_input().split()
N = int(NWH[0])
W = int(NWH[1])
H = int(NWH[2])

# Création d'une liste d'adjacence vide
E = []
for i in range(N):
    E.append([])

# Liste pour stocker les points et un drapeau pour les bords
lst = []
flag = True

for i in range(N):
    xy = raw_input().split()
    x = int(xy[0])
    y = int(xy[1])
    if x == 1 or y == 1 or x == W or y == H:
        flag = False
    lst.append((x, y, i))

# On trie d'abord selon x puis on relie les points qui partagent la même coordonnée x
lst.sort()
for i in range(N):
    if i > 0:
        if lst[i][0] == lst[i - 1][0]:
            a = lst[i][2]
            b = lst[i - 1][2]
            E[a].append(b)
            E[b].append(a)

# On crée une nouvelle liste pour trier selon y cette fois
lst2 = []
for i in range(N):
    x = lst[i][0]
    y = lst[i][1]
    idx = lst[i][2]
    lst2.append((y, x, idx))

lst = lst2
lst.sort()
for i in range(N):
    if i > 0:
        if lst[i][0] == lst[i - 1][0]:
            a = lst[i][2]
            b = lst[i - 1][2]
            E[a].append(b)
            E[b].append(a)

# On garde une trace des points déjà visités
used = []
for i in range(N):
    used.append(False)

# Fonction DFS basique
def func(num, pre):
    if used[num]:
        return
    used[num] = True
    for to in E[num]:
        if to != pre:
            func(to, num)

cnt = 0
for i in range(N):
    if not used[i]:
        func(i, -1)
        cnt = cnt + 1

if cnt > 1 and flag:
    cnt = cnt + 1

print N - 2 + cnt
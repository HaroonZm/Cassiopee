from collections import deque

# Lecture des entrées
NWH = raw_input().split()
N = int(NWH[0])
W = int(NWH[1])
H = int(NWH[2])

E = []
for i in range(N):
    E.append([])

lst = []
flag = True

# Lecture des points
for i in range(N):
    xy = raw_input().split()
    x = int(xy[0])
    y = int(xy[1])
    if x == 1 or y == 1 or x == W or y == H:
        flag = False
    lst.append((x, y, i))

# On trie la liste par x puis on connecte les voisins ayant le même x
lst.sort()
for i in range(N):
    if lst[i][0] == lst[i-1][0]:
        E[lst[i][2]].append(lst[i-1][2])
        E[lst[i-1][2]].append(lst[i][2])

# On refait la même chose en inversant x et y (pour traiter la colonne)
lst2 = []
for i in range(N):
    x, y, idx = lst[i]
    lst2.append((y, x, idx))
lst = lst2
lst.sort()
for i in range(N):
    if lst[i][0] == lst[i-1][0]:
        E[lst[i][2]].append(lst[i-1][2])
        E[lst[i-1][2]].append(lst[i][2])

# DFS pour compter les composantes connexes
used = []
for i in range(N):
    used.append(False)

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
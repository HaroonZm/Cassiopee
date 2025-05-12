import random

n = int(input())
a = [list(input()) for _ in range(n)]

e = [0 for _ in range(n)]
kachi = [0 for _ in range(n)]
hikiwake = [0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j] == 'o':
            e[i] += 3 / n
            kachi[i] += 1
        elif a[i][j] == '-':
            e[i] += 1 / n
            hikiwake[i] += 1

me = -1
idx = -1
for i in range(n):
    if me < e[i]:
        me = e[i]
        idx = i

ls = []
for i in range(n):
    if a[i][idx] == 'o':
        ls.append(i + 1)

if len(ls) == 0:
    ls.append(idx + 1)

for i in range(1000):
    print(ls[i % len(ls)])
    s = input()
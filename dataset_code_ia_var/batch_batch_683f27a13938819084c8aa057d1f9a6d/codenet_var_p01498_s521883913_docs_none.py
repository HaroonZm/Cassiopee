from collections import deque
import itertools as it
import sys
import math

N, W, H = map(int, raw_input().split())

E = [[] for i in range(N)]
lst = []
flag = True

for i in range(N):
    x, y = map(int, raw_input().split())
    if x == 1 or y == 1 or x == W or y == H:
        flag = False
    lst.append((x, y, i))

lst.sort()
for i in range(N):
    if lst[i][0] == lst[i - 1][0]:
        E[lst[i][2]].append(lst[i - 1][2])
        E[lst[i - 1][2]].append(lst[i][2])

lst2 = []

for i in range(N):
    x, y, index = lst[i]
    lst2.append((y, x, index))

lst = lst2
lst.sort()
for i in range(N):
    if lst[i][0] == lst[i - 1][0]:
        E[lst[i][2]].append(lst[i - 1][2])
        E[lst[i - 1][2]].append(lst[i][2])

used = [False for i in range(N)]

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
        cnt += 1

if cnt > 1 and flag:
    cnt += 1
print N - 2 + cnt
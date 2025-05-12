from sys import stdin, stdout
import math
import bisect
import queue

w, d, n = map(int, input().strip().split())

mapper = [[-1000 for i in range(55)] for j in range(55)]
step = [[0, 1], [0, -1], [1, 0], [-1, 0]]

arr = []

for i in range(n):
    tmp = tuple(map(int, stdin.readline().strip().split()))
    arr.append(tmp)

flag = 1

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1]) < abs(arr[i][2] - arr[j][2]):
            flag = 0
            break
    if flag == 0:
        break

if flag == 0:
    stdout.writelines('No\n')
else:
    for each in arr:
        mapper[each[0]][each[1]] = each[2]
        chk = [[0 for i in range(55)] for j in range(55)]
        chk[each[0]][each[1]] = 1
        pend = queue.Queue()
        pend.put(each)
        while pend.qsize():
            top = pend.get()
            for each in step:
                newpos = [top[0] - each[0], top[1] - each[1]]
                if newpos[0] > 0 and newpos[0] <= w and newpos[1] > 0 and newpos[1] <= d and chk[newpos[0]][newpos[1]] < 1:
                    mapper[newpos[0]][newpos[1]] = max(mapper[newpos[0]][newpos[1]], top[2] - 1)
                    chk[newpos[0]][newpos[1]] += 1
                    pend.put((newpos[0], newpos[1], mapper[newpos[0]][newpos[1]]))
    ans = 0
    for i in range(1, w + 1):
        for j in range(1, d + 1):
            ans += mapper[i][j]
    stdout.writelines(str(ans) + '\n')
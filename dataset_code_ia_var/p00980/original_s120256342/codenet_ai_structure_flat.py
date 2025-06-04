from sys import stdin, stdout
import math
import bisect
import queue

w, d, n = map(int, input().strip().split())

mapper = []
for i in range(55):
    temp_row = []
    for j in range(55):
        temp_row.append(-1000)
    mapper.append(temp_row)

step = [[0, 1], [0, -1], [1, 0], [-1, 0]]

arr = []
for i in range(n):
    line = stdin.readline()
    while line.strip() == "":
        line = stdin.readline()
    tmp = tuple(map(int, line.strip().split()))
    arr.append(tmp)

flag = 1
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        a1, b1, c1 = arr[i]
        a2, b2, c2 = arr[j]
        diff = abs(a1 - a2) + abs(b1 - b2)
        val = abs(c1 - c2)
        if diff < val:
            flag = 0
            break
    if flag == 0:
        break

if flag == 0:
    stdout.writelines('No\n')
else:
    for idxarr in range(len(arr)):
        each = arr[idxarr]
        x, y, v = each
        mapper[x][y] = v
        chk = []
        for i in range(55):
            chkrow = []
            for j in range(55):
                chkrow.append(0)
            chk.append(chkrow)
        chk[x][y] = 1
        pend = queue.Queue()
        pend.put((x, y, v))
        while pend.qsize():
            top = pend.get()
            for istep in range(len(step)):
                s = step[istep]
                newx = top[0] - s[0]
                newy = top[1] - s[1]
                if newx > 0 and newx <= w and newy > 0 and newy <= d and chk[newx][newy] < 1:
                    newval = top[2] - 1
                    if mapper[newx][newy] < newval:
                        mapper[newx][newy] = newval
                    chk[newx][newy] += 1
                    pend.put((newx, newy, mapper[newx][newy]))
    ans = 0
    i = 1
    while i <= w:
        j = 1
        while j <= d:
            ans += mapper[i][j]
            j += 1
        i += 1
    stdout.writelines(str(ans) + '\n')
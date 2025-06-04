N = int(input())
Xsize = 1001
Ysize = 1001

Data = []
for y in range(Ysize):
    Data.append([0] * Xsize)

Tmp = []
for y in range(Ysize):
    Tmp.append([0] * Xsize)

Ans = []
for y in range(Ysize):
    Ans.append([0] * Xsize)

for i in range(N):
    line = input().split()
    x1 = int(line[0])
    y1 = int(line[1])
    x2 = int(line[2])
    y2 = int(line[3])
    Data[y1][x1] += 1
    Data[y1][x2] -= 1
    Data[y2][x1] -= 1
    Data[y2][x2] += 1

for y in range(Ysize):
    Tmp[y][0] = Data[y][0]
    for x in range(1, Xsize):
        Tmp[y][x] = Tmp[y][x-1] + Data[y][x]

for x in range(Xsize):
    Ans[0][x] = Tmp[0][x]
    for y in range(1, Ysize):
        Ans[y][x] = Ans[y-1][x] + Tmp[y][x]

ans = 0
for y in range(Ysize):
    now_max = 0
    for x in range(Xsize):
        if Ans[y][x] > now_max:
            now_max = Ans[y][x]
    if now_max > ans:
        ans = now_max

print(ans)
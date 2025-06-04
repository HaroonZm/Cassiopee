import sys

point = list(map(int, input().split()))
if point[0] == 0 and point[1] == 0:
    print("1")
    sys.exit()
fiblist = [0, 1, 1]
maxpoint = [0, 0]
minpoint = [0, 0]
i = 2
while True:
    if i % 4 == 2 or i % 4 == 3:
        maxpoint[i % 2] += fiblist[2]
    else:
        minpoint[i % 2] -= fiblist[2]
    if minpoint[0] <= point[0] and maxpoint[0] >= point[0] and minpoint[1] <= point[1] and maxpoint[1] >= point[1]:
        print((i - 1) % 3 + 1)
        break
    fiblist[0] = fiblist[1]
    fiblist[1] = fiblist[2]
    fiblist[2] = fiblist[0] + fiblist[1]
    i += 1
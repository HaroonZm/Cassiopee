tbl = []
for i in range(1111):
    tbl.append(i**3)

while True:
    z = int(input())
    if z == 0:
        break
    ma = 0
    x = z - 1
    while x > 0:
        target = tbl[z] - tbl[x]
        y = 0
        for i in range(len(tbl)):
            if tbl[i] > target:
                break
            y = i
        if tbl[y] > tbl[x]:
            break
        if tbl[x] + tbl[y] > ma:
            ma = tbl[x] + tbl[y]
        x = x - 1
    print(tbl[z] - ma)
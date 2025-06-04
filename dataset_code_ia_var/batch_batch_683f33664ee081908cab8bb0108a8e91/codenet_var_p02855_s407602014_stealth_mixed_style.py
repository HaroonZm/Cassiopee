h,w,k = [int(x) for x in input().split()]
s = []
for _ in range(h):
    row_str = input()
    temp = []
    idx = 0
    while idx < len(row_str):
        temp.append(row_str[idx])
        idx += 1
    s.append(temp)

result = []
for a in range(h):
    buf = []
    for b in range(w):
        buf.append(0)
    result.append(buf)

cc = 1
for y in range(h):
    x = 0
    while x < w:
        if s[y][x] == "#":
            result[y][x] = cc
            cc += 1
        x += 1

for y in range(h):
    run = None
    for x in range(w):
        if result[y][x]:
            run = result[y][x]
        elif run:
            result[y][x] = run

for y in range(h):
    x = w-1
    run = None
    while x >= 0:
        if result[y][x]:
            run = result[y][x]
        elif run:
            result[y][x] = run
        x -= 1

for y in range(h):
    for x in range(w):
        if not result[y][x]:
            if y > 0:
                result[y][x] = result[y-1][x]

for _ in range(h):
    j = w-1
    i = h-1 - _
    while j >= 0:
        if result[i][j] == 0:
            if i < h-1:
                result[i][j] = result[i+1][j]
        j -= 1

[print(*row) for row in result]
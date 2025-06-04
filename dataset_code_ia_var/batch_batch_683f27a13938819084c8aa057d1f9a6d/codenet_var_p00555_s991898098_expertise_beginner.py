n, m, d = map(int, input().split())

floor = []
for i in range(n):
    line = input()
    row = []
    for ch in line:
        row.append(ch)
    floor.append(row)

count = 0

for i in range(n):
    for j in range(m):
        if floor[i][j] == ".":
            ok = True
            for k in range(1, d):
                if j+k >= m or floor[i][j+k] != ".":
                    ok = False
                    break
            if ok:
                count += 1

            ok2 = True
            for k in range(1, d):
                if i+k >= n or floor[i+k][j] != ".":
                    ok2 = False
                    break
            if ok2:
                count += 1

print(count)
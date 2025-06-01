w, h = input().split()
w = int(w)
h = int(h)

col_str = input().split()
row_str = input().split()

col = []
row = []

for i in col_str:
    col.append(int(i))

for i in row_str:
    row.append(int(i))

sumC = 0
sumR = 0

for c in col:
    sumC = sumC + c

for r in row:
    sumR = sumR + r

if sumR != sumC:
    print(0)
    exit()

for i in range(w):
    row.sort(reverse=True)
    for j in range(h):
        if col[i] == 0 or row[j] == 0:
            break
        row[j] = row[j] - 1
        col[i] = col[i] - 1
    if col[i] > 0:
        print(0)
        exit()

print(1)
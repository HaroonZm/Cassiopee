r, c = map(int, input().split())
sheet = []
i = 0
while i < r:
    row = []
    values = input().split()
    j = 0
    while j < c:
        row.append(int(values[j]))
        j += 1
    rsum = 0
    j = 0
    while j < c:
        rsum += row[j]
        j += 1
    row.append(rsum)
    sheet.append(row)
    k = 0
    s = []
    while k < len(row):
        s.append(str(row[k]))
        k += 1
    print(' '.join(s))
    i += 1

row = []
j = 0
while j < c + 1:
    csum = 0
    i = 0
    while i < r:
        csum += sheet[i][j]
        i += 1
    row.append(csum)
    j += 1
k = 0
s = []
while k < len(row):
    s.append(str(row[k]))
    k += 1
print(' '.join(s))
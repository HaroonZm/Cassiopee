r, c = map(int, input().split())
sheet = []
i = 0
while i < r:
    row = list(map(int, input().split()))
    sheet.append(row)
    i += 1

i = 0
while i < r:
    s = 0
    j = 0
    while j < c:
        s += sheet[i][j]
        j += 1
    sheet[i].append(s)
    i += 1

sum_list = []
i = 0
while i < c + 1:
    s = 0
    j = 0
    while j < r:
        s += sheet[j][i]
        j += 1
    sum_list.append(s)
    i += 1

sheet.append(sum_list)

i = 0
while i < r + 1:
    j = 0
    while j < c + 1:
        if j != c:
            print(sheet[i][j], end=' ')
        else:
            print(sheet[i][j], end='')
        j += 1
    print()
    i += 1
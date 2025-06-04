r, c = [int(i) for i in input().split()]
table = []
for _ in range(r):
    row = list(map(int, input().split()))
    table.append(row)
for i in range(r):
    s = 0
    for j in range(c):
        s += table[i][j]
    table[i].append(s)
last_row = []
for j in range(c+1):
    s = 0
    for i in range(r):
        s += table[i][j]
    last_row.append(s)
table.append(last_row)
for i in range(r+1):
    for j in range(c+1):
        print(table[i][j], end=' ')
    print()
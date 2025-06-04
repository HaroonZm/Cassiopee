table = []
for i in range(2001):
    row = []
    for j in range(2001):
        row.append(0)
    table.append(row)

x1, y1, w1, h1 = input().split()
x1 = int(x1)
y1 = int(y1)
w1 = int(w1)
h1 = int(h1)

x2, y2, w2, h2 = input().split()
x2 = int(x2)
y2 = int(y2)
w2 = int(w2)
h2 = int(h2)

ans = 0

i = x1
while i < x1 + w1:
    j = y1
    while j < y1 + h1:
        table[i][j] = 1
        ans = ans + 1
        j = j + 1
    i = i + 1

i = x2
while i < x2 + w2:
    j = y2
    while j < y2 + h2:
        if table[i][j] == 0:
            table[i][j] = 1
            ans = ans + 1
        else:
            table[i][j] = 0
            ans = ans - 1
        j = j + 1
    i = i + 1

print(ans)
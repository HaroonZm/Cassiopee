r, c = map(int,input().split())
sheet = []
for i in range(0,r):
    row = []
    row[:] = map(int,input().split())
    rsum = 0
    for j in range(0,c):
        rsum+=row[j]
    row.append(rsum)
    sheet.append(row)
    print(' '.join(map(str,row)))

row = []
for j in range(0,c+1):
    csum = 0
    for i in range(0,r):
        csum+=sheet[i][j]
    row.append(csum)
print(' '.join(map(str,row)))
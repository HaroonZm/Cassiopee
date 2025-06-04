n = int(input())
d = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(0)
    d.append(row)

for i in range(1, n+1):
    s = str(i)
    if s[0] == "0" or s[-1] == "0":
        continue
    d[int(s[0])][int(s[-1])] = d[int(s[0])][int(s[-1])] + 1

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans = ans + d[i][j] * d[j][i]

print(ans)
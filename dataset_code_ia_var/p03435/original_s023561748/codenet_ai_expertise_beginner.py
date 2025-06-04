c = []
for i in range(3):
    row = input().split()
    row = [int(x) for x in row]
    c.append(row)

res = 0
ans = 0

for i in range(3):
    res = res + sum(c[i])
    ans = ans + c[i][i] * 3

if res == ans:
    print('Yes')
else:
    print('No')
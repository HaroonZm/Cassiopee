h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

order = []
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            order.append((i, j))
    else:
        for j in range(w-1, -1, -1):
            order.append((i, j))

colors = []
for i in range(n):
    for j in range(a[i]):
        colors.append(i+1)

result = []
for i in range(h):
    row = []
    for j in range(w):
        row.append(0)
    result.append(row)

for idx in range(len(order)):
    i, j = order[idx]
    result[i][j] = colors[idx]

for row in result:
    print(' '.join(str(x) for x in row))
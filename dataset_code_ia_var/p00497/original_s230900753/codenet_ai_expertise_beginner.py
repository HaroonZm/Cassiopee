n, m = map(int, input().split())

abx = []
for i in range(n+2):
    abx.append([0] * (n+2))

for i in range(m):
    a, b, x = map(int, input().split())
    if abx[a][b] < x:
        abx[a][b] = x

pp = []
for i in range(n+2):
    pp.append([0] * (n+2))

for j in range(1, n+2):
    queue = []
    for i in range(j, n+2):
        if abx[i][j] > 0:
            queue.append([i, abx[i][j]])
    last = j - 1
    while len(queue) > 0:
        ii, xi = queue.pop(0)
        if ii + xi > last:
            for iii in range(max(ii, last+1), ii+xi+1):
                pp[iii][j] = iii - ii + 1
                last = iii

count = 0
for i in range(1, n+1):
    for j in range(1, i+1):
        abij = pp[i][j-1] - 1
        pp[i][j] = max(pp[i][j], abij)
        if pp[i][j] > 0:
            count += 1

print(count)
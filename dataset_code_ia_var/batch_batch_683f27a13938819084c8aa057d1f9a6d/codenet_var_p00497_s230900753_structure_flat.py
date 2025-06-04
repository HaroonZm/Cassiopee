from collections import deque

n, m = map(int, input().split())
abx = []
for i in range(n + 2):
    abx.append([0] * (n + 2))
for _ in range(m):
    ai, bi, xi = map(int, input().split())
    if abx[ai][bi] < xi:
        abx[ai][bi] = xi

pp = []
for i in range(n + 2):
    pp.append([0] * (n + 2))

j = 1
while j < n + 2:
    dq = deque()
    i = j
    while i < n + 2:
        if abx[i][j] > 0:
            dq.append([i, abx[i][j]])
        i += 1
    iiii = j - 1
    while len(dq) > 0:
        temp = dq.popleft()
        ii = temp[0]
        xi = temp[1]
        if ii + xi > iiii:
            iii = max(ii, iiii + 1)
            while iii < ii + xi + 1:
                pp[iii][j] = iii - ii + 1
                iiii = iii
                iii += 1
    j += 1

icnt = 0
i = 1
while i < n + 1:
    j = 1
    while j < i + 1:
        abij = pp[i][j - 1] - 1
        if pp[i][j] < abij:
            pp[i][j] = abij
        if pp[i][j] > 0:
            icnt += 1
        j += 1
    i += 1

print(icnt)
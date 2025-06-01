from collections import deque
import sys

input_line = sys.stdin.readline
n,m = map(int, input_line().split())
abx = [[0 for _ in range(n+2)] for _ in range(n+2)]

for _ in range(m):
    ai, bi, xi = map(int, input_line().split())
    abx[ai][bi] = max(abx[ai][bi], xi)

pp = list(map(lambda _: [0]*(n+2), range(n+2)))

j = 1
while j < n+2:
    dq = deque()
    i = j
    while i < n+2:
        if abx[i][j] > 0:
            dq.append([i, abx[i][j]])
        i += 1

    iiii = j - 1
    while len(dq) > 0:
        ii, xi = dq.popleft()
        if ii + xi > iiii:
            for iii in range(max(ii, iiii + 1), ii + xi + 1):
                pp[iii][j] = iii - ii + 1
                iiii = iii
    j += 1

icnt = 0
for i in range(1, n+1):
    j = 1
    while j <= i:
        abij = pp[i][j-1] - 1
        if pp[i][j] < abij:
            pp[i][j] = abij
        if pp[i][j] > 0:
            icnt += 1
        j += 1

print(icnt)
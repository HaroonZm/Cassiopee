d = int(input())
c = list(map(int, input().split()))
s = []
for _ in range(d):
    s.append(list(map(int, input().split())))
t = []
cnt = 0
while cnt < d:
    t.append(int(input()))
    cnt += 1
m = int(input())
dp = []
for __ in range(m):
    dp += [list(map(int, input().split()))]

Score = dict((i, 0) for i in range(26))
Last = {}
for i in range(26):
    Last[i] = -1

ii = 0
while ii < d:
    idx = t[ii]-1
    Score[idx] += s[ii][idx]
    Last[idx] = ii
    for j in range(26):
        Score[j] -= c[j] * (ii - Last[j])
    ii += 1

for k in range(m):
    xx = t[dp[k][0]-1]
    yy = dp[k][1]
    t[dp[k][0]-1] = yy
    for num in [xx, yy]:
        Score[num-1] = 0
        Last[num-1] = -1
    i = 0
    while i < d:
        if t[i] == xx or t[i] == yy:
            Score[t[i]-1] += s[i][t[i]-1]
            Last[t[i]-1] = i
        Score[xx-1] -= c[xx-1] * (i - Last[xx-1])
        Score[yy-1] -= c[yy-1] * (i - Last[yy-1])
        i += 1
    print(sum(list(Score.values())))
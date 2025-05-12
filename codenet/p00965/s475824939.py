n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

pol1 = 0
pol2 = 0

ft = [[0] * 2 for _ in range(100000)] 

for i in ab:
    ft[i[0] - 1][0] += 1
    ft[i[1] - 1][1] += 1

ftsum = [[0] * 2 for _ in range(100000)]
ftsum[0][0] = ft[0][0]
for i in range(1, len(ft)):
    ftsum[i][0] = ftsum[i-1][0] + ft[i][0]
    ftsum[i][1] = ftsum[i-1][1] + ft[i][1]

for i in range(len(ft)-1):
    pol2 = max(pol2, ftsum[i][0] - ftsum[i][1])

for f, t in ab:
    f = f-1
    t = t-1
    temp = ftsum[t-1][0]
    if f != 0:
        temp -= ftsum[f][1]
    pol1 = max(pol1, temp)

print(pol1, pol2)
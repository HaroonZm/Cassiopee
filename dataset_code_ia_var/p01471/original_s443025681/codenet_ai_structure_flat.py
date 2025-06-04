ri = (raw_input()).split(" ")
n = int(ri[0])
w = int(ri[1])
d = [0] * n
dp = []
dm = []
restrict = 0.0
result = 0.0

i = 0
while i < n:
    ri = (raw_input()).split(" ")
    d[i] = [0] * 3
    d[i][1] = int(ri[0]) * 1.0  # w
    d[i][2] = int(ri[1]) * 1.0  # v
    if d[i][1] <= 0 and d[i][2] >= 0:
        restrict += d[i][1]
        result += d[i][2]
    elif d[i][1] > 0 and d[i][2] > 0:
        dp.append([1.0 * d[i][1] / d[i][2], d[i][1], d[i][2], 0.0])
    elif d[i][1] < 0 and d[i][2] < 0:
        dm.append([-1.0 * d[i][1] / d[i][2], d[i][1], d[i][2], 0.0])
    i += 1

dp = sorted(dp)
dm = sorted(dm)
dmidx = 0
i = 0
while i < len(dp):
    if dp[i][1] + restrict <= w:
        restrict += dp[i][1]
        result += dp[i][2]
        dp[i][3] = 1.0
    else:
        dp[i][3] = 1.0 * (w - restrict) / dp[i][1]
        restrict = w
        result += dp[i][2] * dp[i][3]
        cont = False
        if len(dm) > 0 and (dp[i][0] < (-dm[dmidx][0])):
            cont = True
        while cont:
            if (1 - dp[i][3]) * dp[i][1] / (-dm[dmidx][1]) < 1 - dm[dmidx][3]:
                dm[dmidx][3] += (1 - dp[i][3]) * dp[i][1] / (-dm[dmidx][1])
                result += (1 - dp[i][3]) * (dp[i][2] - dm[dmidx][2] * dp[i][1] / dm[dmidx][1])
                dp[i][3] = 1.0
                cont = False
            else:
                dp[i][3] += (1 - dm[dmidx][3]) * (-dm[dmidx][1]) / dp[i][1]
                result += (1 - dm[dmidx][3]) * (dm[dmidx][2] + dp[i][2] * (-dm[dmidx][1]) / dp[i][1])
                dm[dmidx][3] = 1.0
                dmidx += 1
                if dmidx >= len(dm):
                    cont = False
                elif dp[i][0] >= (-dm[dmidx][0]):
                    cont = False
    i += 1

print(result)
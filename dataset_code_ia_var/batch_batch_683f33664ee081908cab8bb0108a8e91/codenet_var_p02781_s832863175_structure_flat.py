import sys
import collections as cl
import bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
mod = 10**9+7
Max = sys.maxsize

n = int(input())
k = int(input())
s = str(n)
L = len(s)
dp0 = []
dp1 = []
for i in range(L+1):
    dp0.append([0,0,0,0])
    dp1.append([0,0,0,0])

po = 0
dp0[0][0] = 0
dp1[0][0] = 1

i = 1
while i <= L:
    point = i-1
    np = int(s[point])
    if np == 0:
        po += 1

    dp0[i][0] = 1
    dp1[i][0] = 0

    if np - 1 > 0:
        a = np - 1
    else:
        a = 0
    dp0[i][1] = dp1[i-1][0]*a + dp0[i-1][0]*9 + dp0[i-1][1]
    if np != 0:
        dp0[i][1] += dp1[i-1][1]
    if i == 1 + po:
        dp1[i][1] = 1
    else:
        dp1[i][1] = 0

    dp0[i][2] = dp1[i-1][1]
    if np - 1 > 0:
        dp0[i][2] *= (np-1)
    else:
        dp0[i][2] *= 0
    dp0[i][2] += dp0[i-1][1]*9 + dp0[i-1][2]
    if np != 0:
        dp0[i][2] += dp1[i-1][2]
    if i == 2 + po:
        dp1[i][2] = 1
    else:
        dp1[i][2] = 0

    dp0[i][3] = dp1[i-1][2]
    if np - 1 > 0:
        dp0[i][3] *= (np-1)
    else:
        dp0[i][3] *= 0
    dp0[i][3] += dp0[i-1][2]*9 + dp0[i-1][3]
    if np != 0:
        dp0[i][3] += dp1[i-1][3]
    if i == 3 + po:
        dp1[i][3] = 1
    else:
        dp1[i][3] = 0
    i += 1

print(dp0[-1][k]+dp1[-1][k])
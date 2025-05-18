from operator import itemgetter
#@profile
def calc(w,pdp,pl,pr,dp,l,r):
    if l >= r:
        return
    m = (l + r) // 2
    dp[m], i = min([(pdp[i] + w[i+1][m],i) for i in range(pl,min(m,pr))], key=itemgetter(0))
    calc(w,pdp,pl,i+1,dp,l,m)
    calc(w,pdp,i,pr,dp,m+1,r)
    return dp

import sys
f = sys.stdin

s,n,m = map(int, f.readline().split())
x = list(map(int, f.readline().split()))
tp = [list(map(int, line.split())) for line in f]

c = [ti - x[pi - 1] for ti, pi in tp]
c.sort()
min_c = c[0]
c = [ci - min_c for ci in c]
d = c[:] 
for i in range(1,len(d)):
    d[i] += d[i - 1]

w = [[0 for j in range(n)] for i in range(n)]
for j in range(1, n):
    for i in range(j): 
        w[i][j] = c[j] * (j - i + 1) - (d[j] - d[i] + c[i])

dp = w[0][:]
for bus in range(2,m + 1):
    pdp = dp 
    dp = [0] * len(pdp)
    pl = bus - 2
    pr = n-m+bus
    if pl > pr:
        continue
    dp = calc(w,pdp,pl,pr,dp,bus,n)
        
print(dp[-1])
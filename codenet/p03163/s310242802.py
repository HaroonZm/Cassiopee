from collections import defaultdict
 
N,W = map(int, input().split())
WV = []
for i in range(N):
    WV.append(list(map(int, input().split())))
 
dp = defaultdict(int)
 
dp[0] = 0
 
for w,v in WV:
    for nw, nv in list(dp.items()):
        if nw+w <= W:
            dp[nw+w] = max(dp[nw+w], nv+v)
            
print(max(dp.values()))
#!/usr/bin/env python3

import bisect
#D2
n = int(input())
a = [int(input()) for j in range(n)]
 
dp = [a[0]]
for i in range(1,n):
    if dp[-1] < a[i]:
        dp.append(a[i])
        #print(0,dp)
 
    else:
        dp[bisect.bisect_left(dp, a[i])] = a[i]
        #print(1,bisect.bisect_left(dp, a[i]),dp)
print(len(dp))
from sys import stdin
from math import comb

dp = [[[0]*(101) for _ in range(10)] for __ in range(101)]
dp[0][0][0]=1
for num in range(101):
    for count in range(9):
        for summ in range(101):
            if dp[num][count][summ]==0:
                continue
            dp[num+1][count][summ]+=dp[num][count][summ]
            if summ+num<=100:
                dp[num+1][count+1][summ+num]+=dp[num][count][summ]

for line in stdin:
    n,s=map(int,line.split())
    if n==0 and s==0:
        break
    if s>100:
        print(0)
        continue
    print(dp[101][n][s])
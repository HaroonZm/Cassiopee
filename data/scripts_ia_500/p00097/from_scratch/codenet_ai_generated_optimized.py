from sys import stdin

MAX_NUM = 100
MAX_N = 9
MAX_S = 1000

# dp[n][s] = nombre de combinaisons pour n éléments distincts dont la somme est s
dp = [[0]*(MAX_S+1) for _ in range(MAX_N+1)]
dp[0][0] = 1

for num in range(MAX_NUM+1):
    for n in range(MAX_N,0,-1):
        for s in range(MAX_S,num-1,-1):
            dp[n][s] += dp[n-1][s-num]

for line in stdin:
    n,s = map(int,line.split())
    if n==0 and s==0:
        break
    print(dp[n][s])
# AOJ 1209: Square Coins
#Python3 2018.7.19 bal4u
 
dp = [1]*300
for i in range(2, 18):
    for j in range(i**2, 300): dp[j] += dp[j-i**2]
 
while True:
    n = int(input())
    if n == 0: break
    print(dp[n])
dp=[1]*301
for i in range(2,18):
    for j in range(i*i,301):dp[j]+=dp[j-i*i]
while 1:
    n=int(input())
    if n==0:break
    print(dp[n])
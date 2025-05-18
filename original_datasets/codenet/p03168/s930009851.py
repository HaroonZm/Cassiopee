n = int(input())

v = list(map(float, input().split()))

dp = [[0.0] * (len(v)+1) for i in range(len(v))]
for x in range(n):
	for a in range(x + 2):
		if x == 0 and a == 0:
			dp[x][a]=v[x]
		elif x == 0 and a == 1 and n != 1:
			dp[x][a]=1-v[x]
		elif a > n/2:
			dp[x][a]=dp[x-1][a]*v[x]
		else:
			dp[x][a]=dp[x-1][a]*v[x]+dp[x-1][a-1]*(1-v[x])
#import numpy
#print(numpy.matrix(dp));			
print(sum(dp[n-1]))
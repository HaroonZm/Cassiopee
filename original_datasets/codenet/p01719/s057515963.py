from collections import defaultdict as ddict
n, d, x = map(int,raw_input().split(" "))
p = [map(int,raw_input().split(" ")) for i in range(d)]
for i in range(d-1):
	profit = ddict(int)
	for j in range(n):
		tmp = p[i+1][j] - p[i][j]
		if tmp > 0 and p[i][j] <= x and tmp > profit[p[i][j]]:
			profit[p[i][j]] = tmp
	dp = [0 for j in range(x+1)]
	for cost, prof in profit.iteritems():
		for j in range(cost,x+1):
			dp[j] = max(dp[j], dp[j-1], dp[j-cost]+prof)
	x += dp[x]
print x
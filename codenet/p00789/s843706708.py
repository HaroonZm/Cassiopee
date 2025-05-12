dp = [1] + [0]*300
for c in range(1,18):
	for i in range(301-c**2):
			dp[i+c**2] += dp[i]
while 1:
	n = input()
	if n == 0: break
	print dp[n]
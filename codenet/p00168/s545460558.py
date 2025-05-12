from math import ceil
dp = [1] + [0 for i in range(33)]
for i in range(0,30):
	for step in [1,2,3]:
		dp[i+step] += dp[i]
unit = 3650.
while 1:
	n = int(raw_input())
	if n == 0:
		break
	print int(ceil(dp[n] / unit))
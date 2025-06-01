from math import ceil
dp = [1] + [0]*33
for i in range(30):
	for step in [1,2,3]:
		dp[i+step] += dp[i]
unit = 3650.
while True:
	n = int(raw_input())
	if n == 0:
		break
	print int(ceil(dp[n]/unit))
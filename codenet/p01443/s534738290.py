s = [0] * 100100
dp = [0] * 100100
t = [10**i for i in range(10)]
	
while 1:
	a,b,p = map(int,raw_input().split())
	if a == b == p == 0: break
	ans = 0
	for i in range(b - a + 1):
		dp[i] = 1
		m = (a + i) / 10
		while a <= m and m <= b:
			dp[i] += s[m - a]
			dp[i] %= p
			m /= 10
		for j in range(10):
			if a + i == t[j]:
				s[i] = dp[i]
				break
		else:
			dp[i] += s[i - 1] if i > 0 else 0
			dp[i] %= p
			s[i] = s[i - 1] + dp[i] if i > 0 else dp[i]
			s[i] %= p
		ans += dp[i]
		ans %= p
	print ans
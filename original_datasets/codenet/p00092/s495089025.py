# don't know good 参考:http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=2954794#1

table = [''] * 1002
dp = [[0] * 1002 for i in range(1002)]

while 1:
	n = int(input())
	if n == 0: break
	for r in range(n): table[r] = input()
	ans = 0
	
	for r in range(n):
		for c in range(n):
			if table[r][c] == '*': dp[r][c] = 0
			else :
				t = dp[r-1][c-1]
				if dp[r  ][c-1] < t: t = dp[r  ][c-1];
				if dp[r-1][c  ] < t: t = dp[r-1][c  ];
				t += 1
				dp[r][c] = t
				if t > ans: ans = t
	print(ans)
r = 1121
p = [1]*r
p[0] = p[1] = 0
for i in range(int(r**0.5)):
	if p[i]:
		p[2*i::i] = [0 for x in range(2*i,r,i)]
prime = []
for i in range(r):
	if p[i]: prime.append(i)

dp = [[0]*r for i in range(15)]
dp[0][0] = 1
for i in range(len(prime)):
	for k in range(min(i+1,14),0,-1):
		for j in range(prime[i],r):
			dp[k][j] += dp[k-1][j-prime[i]]

while 1:
	n,k = map(int,raw_input().split())
	if n == 0: break
	print dp[k][n]
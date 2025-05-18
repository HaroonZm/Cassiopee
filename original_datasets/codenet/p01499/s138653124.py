from collections import Counter
MOD = 10**9+7
n, t = map(int, input().split())
d = [int(input()) for _ in range(n)]
d.sort(reverse=True)
c = Counter(d)
cum = [0 for _ in range(200002)]
for i in range(100000, 0, -1):
	cum[i] = cum[i+1] + c[i]
ans = 1
for i, x in enumerate(d):
	mul = i+1 - cum[x+t+1]
	ans *= mul
	ans %= MOD
print(ans)
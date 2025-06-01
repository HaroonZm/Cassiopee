# AOJ 0150 Twin Prime
# Python3 2018.6.17 bal4u

MAX = 10001
SQRT = 100     # sqrt(MAX)

prime = [True]*MAX
def sieve():
#	for i in range(4, MAX, 2):
#		prime[i] = False
	for i in range(3, SQRT, 2):
		if prime[i] is True:
			for j in range(i*i, MAX, i):
				prime[j] = False
sieve()
tbl, ans = [0]*MAX, 0
for i in range(5, MAX, 2):
	if prime[i] and prime[i-2]: ans = i
	tbl[i] = ans
	
while True:
	n = int(input())
	if n == 0: break
	if (n & 1) == 0: n -= 1
	print(tbl[n]-2, tbl[n])
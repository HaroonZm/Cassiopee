# AOJ 0150 Twin Prime
# Python3 2018.6.17 bal4u

MAX = 10000
SQRT = 100     # sqrt(MAX)

prime = [True for i in range(MAX)]
def sieve():
	for i in range(4, MAX, 2):
		prime[i] = False
	for i in range(3, SQRT, 2):
		if prime[i] is True:
			for j in range(i*i, MAX, i):
				prime[j] = False
sieve()
while True:
	n = int(input())
	if n == 0: break
	if (n & 1) == 0: n -= 1
	while not prime[n] or not prime[n - 2]: n -= 2
	print(n-2, n)
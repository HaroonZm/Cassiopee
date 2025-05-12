import math
def sieve (n):
	prime = [0,0]
	prime += [1 for i in range(n-1)]
	ub = math.sqrt(n) + 1
	d = 2
	while d <= ub:
		if prime[d] == 0:
			d += 1
			continue
		prod = 2
		while d * prod <= n:
			prime[d*prod] = 0
			prod += 1
		d += 1
	return prime
prime = sieve(1299709)
while 1:
	k = int(raw_input())
	if k == 0:
		break
	l = r = k
	while prime[l] == 0:
		l -= 1
	while prime[r] == 0:
		r += 1
	print (r-1) - (l+1) + 2
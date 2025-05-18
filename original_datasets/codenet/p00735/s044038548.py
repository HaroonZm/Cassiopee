import sys
def sieve (n):
	ms_sieve = [0,0,0,0,0,0]
	ms_sieve += [1 for i in range(n-5)]
	ms_prime = []
	d = 6
	while d <= n:
		if ms_sieve[d] == 0:
			d += 1
			continue
		if d % 7 != 1 and d % 7 != 6:
			ms_sieve[d] = 0
			d += 1
			continue
		ms_prime.append(d)
		prod = 2
		while d * prod <= n:
			ms_sieve[d*prod] = 0
			prod += 1
		d += 1
	return ms_prime
ms_prime = sieve(300000)
while 1:
	n = int(raw_input())
	if n == 1:
		break
	sys.stdout.write("%d:" % n)
	for msp in ms_prime:
		if msp > n:
			break
		quot, rem = divmod(n,msp)
		if rem != 0:
			continue 
		rem2 = quot % 7
		if rem2 == 1 or rem2 == 6: 
			sys.stdout.write(" %d" % msp)
	print ""
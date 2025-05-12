# AOJ 1026 Hedro's Hexahedron
# Python3 2018.7.5 bal4u

while True:
	n = int(input())
	if n == 0: break
	ans = s = n >> 1
	i, k = 1, 2
	while i*i < s:
		ans += (n+k-1)//k
		i += 1
		k += 2
	ans = ans*2 - i*i
	if n & 1: ans += 1
	print((ans+n) << 3)
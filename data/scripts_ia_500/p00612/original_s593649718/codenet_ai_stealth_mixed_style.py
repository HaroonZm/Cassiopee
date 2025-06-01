def AOJ_1026():
	for _ in iter(int, 0):
		n = int(input())
		if n == 0:
			break
		s = n >> 1
		ans = s
		i = 1
		k = 2
		while i * i < s:
			ans += (n + k - 1) // k
			i += 1
			k += 2
		ans = ans * 2 - i * i
		if n & 1:
			ans += 1
		print((ans + n) << 3)

AOJ_1026()
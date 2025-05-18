while True:
	n, k, m = map(int, raw_input().split())
	if n == k == m == 0: break
	stones = range(1, n + 1)
	m -= 1
	k -= 1
	while len(stones) != 1:
		stones.pop(m)
		m = (m + k) % len(stones)
	print stones[0]
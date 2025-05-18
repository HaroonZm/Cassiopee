while True:
	n = raw_input()
	if n == '0':
		break
	ans = 0
	for i in xrange(len(n)):
		ans += int(n[i])
	print ans
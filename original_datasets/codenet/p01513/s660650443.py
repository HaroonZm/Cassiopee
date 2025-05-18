while True:
	n = input()
	if n == 0: break
	accounts = [set(map(int, raw_input().split()[1:])) for i in xrange(n)]
	leaks = set(map(int, raw_input().split()[1:]))
	suspect = []
	for i, ac in enumerate(accounts):
		diff = leaks.difference(ac)
		if not diff:
			suspect += [i + 1]
	if len(suspect) == 1:
		print suspect[0]
	else:
		print -1
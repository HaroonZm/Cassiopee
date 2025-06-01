while 1:
	k = input()
	if not k: break
	print sum(map(int, raw_input().split()))/(k-1)
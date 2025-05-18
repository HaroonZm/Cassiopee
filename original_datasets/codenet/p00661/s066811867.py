while 1:
	n,m = map(int,raw_input().split())
	if n == 0: break
	p = min(map(int,raw_input().split()))
	print n/2.0 if p > 1 else 0.0
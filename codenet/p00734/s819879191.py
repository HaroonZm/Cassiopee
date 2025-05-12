while 1:
	n,m = map(int,raw_input().split())
	if n == 0: break
	taro = sorted([int(raw_input()) for i in range(n)])
	hana = [int(raw_input()) for i in range(m)]
	d = sum(hana) - sum(taro)
	t,h = 101,101
	for i in taro:
		if d/2.0 + i in hana:
			t,h = i,d/2 + i
			break
	print "%d %d"%(t,h) if t < 101 else -1
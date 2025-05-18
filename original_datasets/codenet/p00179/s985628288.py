rgb = set(["r","g","b"])
while 1:
	worm = raw_input()
	if worm == "0": break
	n = len(worm)
	L = 1
	cnt = flag = 0
	queset = set([worm])
	while 1:
		que = list(queset)
		queset = set()
		for r in range(L):
			Worm = que.pop(0)
			if len(set(Worm)) == 1:
				flag = 1
				break
			for i in range(n-1):
				if Worm[i] != Worm[i+1]:
					nextclr = list(rgb-set(Worm[i:i+2]))[0]
					worm = Worm[:i] + 2*nextclr + Worm[i+2:]
					queset.add(worm)
		L = len(queset)
		if flag: break
		cnt += 1
		if cnt > 15: break
	print cnt if flag else "NA"
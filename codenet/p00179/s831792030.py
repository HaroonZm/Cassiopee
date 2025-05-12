rgb = set(["r","g","b"])
while 1:
	worm = raw_input()
	if worm == "0": break
	n = len(worm)
	que = [worm]
	ref = set(worm)
	L = 1
	cnt = flag = 0
	while 1:
		for r in range(L):
			Worm = que.pop(0)
			if Worm in ref: continue
			else: ref.add(Worm)
			if len(set(Worm)) == 1:
				flag = 1
				break
			for i in range(n-1):
				if Worm[i] != Worm[i+1]:
					worm = Worm[:]
					nextclr = list(rgb-set(worm[i:i+2]))[0]
					worm = worm[:i] + 2*nextclr + worm[i+2:]
					if worm not in que: que.append(worm)
		L = len(que)
		if flag or L == 0: break
		cnt += 1
		if cnt > 15: break
	print cnt if flag else "NA"
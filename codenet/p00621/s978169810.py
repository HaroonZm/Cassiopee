while 1:
	W,Q = map(int,raw_input().split())
	if W == 0: break
	cat = [map(str,raw_input().split()) for i in range(Q)]
	dic = {cat[i][1]:[int(cat[i][2]),0] for i in range(Q) if cat[i][0] == "s"}
	wall = [-1]*W
	for i in range(Q):
		if cat[i][0] == "s":
			id,w = cat[i][1],int(cat[i][2])
			for j in range(W-w+1):
				if wall[j:j+w] == [-1]*w:
					wall[j:j+w] = [id]*w
					dic[id][1] = j
					print j
					break
			else:
				print "impossible"
		else:
			w,sp = dic[cat[i][1]]
			wall[sp:sp+w] = [-1]*w
	print "END"
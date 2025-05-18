def Con(X) :
	# concentration 濃度
	if(r + X * R - C * w  >= 0) :
		return 0
	else :
		return 1

	
while True :
	r, w, C, R = map(int, input().split())
	if(C == 0) :
		break
	else :
		for i in range(10000) :
			if(Con(i) == 0) :
				print(i)
				break
			else :
				pass
MAX = 10**9 * 2
while 1:
	N = int(raw_input())
	if N == 0:
		break
	signal = raw_input().split(" ")
	xst = MAX + 1
	xlt = - xst
	for i in range(N):
		if signal[i] == "x":
			if i < N-1 and signal[i+1] == "x" :
				print "none"
				break
			if (i + 1) % 2 != 0:
				left = MAX + 1 if i <= 0 else int(signal[i-1]) 
				right = MAX + 1 if i >= N-1 else int(signal[i+1])
				xst = min(xst, left, right)
			else :
				left = - (MAX + 1) if i <= 0 else int(signal[i-1]) 
				right = - (MAX + 1) if i >= N-1 else int(signal[i+1])
				xlt = max(xlt, left, right)
		elif i < N-1 and signal[i+1] != "x" :
				if ( (i + 1) % 2 != 0 and int(signal[i]) >= int(signal[i+1]) 
				  or (i + 1) % 2 == 0 and int(signal[i]) <= int(signal[i+1])) :
					print "none"
					break
	else :
		x = "none"
		tmpx = xlt + 1
		while tmpx < xst:
			if x != "none" :
				print "ambiguous"
				break
			x = tmpx
			tmpx += 1
		else :
			print x
while 1:
	n=input()
	if n==0: break
	d=[map(int,raw_input().split()) for i in range(n)]
	w=max([sum([d2[0] for d2 in d if d2[1]<=d1[1]<d2[2]]) for d1 in d])
	print "OK" if w<151 else "NG"
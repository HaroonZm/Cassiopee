while 1:
	m,n=map(str,raw_input().split())
	if m=="0":break
	h=b=0
	for i in range(4):
		if m[i]==n[i]:h+=1
		elif m[i] in n:b+=1
	print h,b
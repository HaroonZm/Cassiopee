while 1:
	a,b = map(int,raw_input().split())
	if a == 0: break
	c = b-a
	t = c/1000
	f = (c-1000*t)/500
	h = (c-1000*t-500*f)/100
	print h,f,t
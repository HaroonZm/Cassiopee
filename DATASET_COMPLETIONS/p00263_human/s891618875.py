for i in range(input()):    
	b=int(raw_input(),16)
	s=1<<31
	p=""
	if b&s!=0:
		b^=s
		p="-"
	a=int(b*1.0/(1<<7))
	print p+str(a)+str(abs(b*1.0/(1<<7)-a))[1:]
while 1:
	n=input()
	if n==0:break
	b=map(int,raw_input().split())
	c=int((b[n-2]*b[n-1]/b[-1])**0.5)
	print c
	print " ".join(map(str,sorted([b[i]/c for i in range(n)])))
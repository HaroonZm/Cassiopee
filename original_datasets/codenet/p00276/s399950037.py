q=input()
for i in [1]*q:
	c,a,n=map(int,raw_input().split())
	s=0
	while c>0 and a>0 and n>0:
		s+=1
		c,a,n=c-1,a-1,n-1
	while c>0 and a>0:
		s+=1
		c,a=c-2,a-1
	print s+c/3
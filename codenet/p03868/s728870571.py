N,*E=map(int,open(0))
a,c=1,0
for _,d in sorted((e,2*(i<N)-1)for i,e in enumerate(E)):
	if c*d<0:a=abs(a*c)%(10**9+7)
	c+=d
print(a)
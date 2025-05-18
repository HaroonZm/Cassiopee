N,W,*L=map(int,open(0).read().split())
d={}
for v,w,m in zip(*[iter(L)]*3):
	d[(v,w)]=d.get((v,w),0)+m
dp=[0]*(W+1)
for (v,w),m in d.items():
	cw,cv=w,v
	b=m.bit_length()
	for i in range(b):
		if i==b-1:
			w=cw*(m-2**(b-1)+1)
			v=cv*(m-2**(b-1)+1)
		for j in range(W,w-1,-1):
			t=dp[j-w]+v
			if t>dp[j]:dp[j]=t
		w*=2
		v*=2
print(dp[W])
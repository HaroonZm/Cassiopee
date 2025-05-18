import sys
readline = sys.stdin.buffer.readline

n,k = map(int,readline().split())
vs = list(map(int,readline().split()))

L=18
xid=[0]*(n*L)
xsum=[0]*(n*L)
yid=[0]*(n*L)
ysum=[0]*(n*L)

j=n
for i in reversed(range(n)):
	while i<j and vs[i]+k<=vs[j-1]:
		j-=1
	xid[i*L+0]=j
	xsum[i*L+0]=j
	for lv in range(1,L):
		a=xid[i*L+lv-1]
		if a==n:
			xid[i*L+lv]=n
		else:
			xid[i*L+lv]=xid[a*L+lv-1]
			xsum[i*L+lv]=xsum[i*L+lv-1]+xsum[a*L+lv-1]

j=-1
for i in range(n):
	while j<i and vs[j+1]+k<=vs[i]:
		j+=1
	yid[i*L+0]=j
	ysum[i*L+0]=j
	for lv in range(1,L):
		a=yid[i*L+lv-1]
		if a==-1:
			yid[i*L+lv]=-1
		else:
			yid[i*L+lv]=yid[a*L+lv-1]
			ysum[i*L+lv]=ysum[i*L+lv-1]+ysum[a*L+lv-1]

q=int(readline())
for tmp in range(q):
	l,r=map(int,readline().split())
	l-=1
	r-=1
	ans=0
	
	i=l
	ans-=i
	for lv in reversed(range(L)):
		if xid[i*L+lv]<=r:
			ans-=xsum[i*L+lv]
			i=xid[i*L+lv]
	
	i=r
	ans+=i+1
	for lv in reversed(range(L)):
		if yid[i*L+lv]>=l:
			ans+=ysum[i*L+lv]+(1<<lv)
			i=yid[i*L+lv]
	
	print(ans)
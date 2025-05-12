from heapq import*
n,*a=map(int,open(0).read().split())
hq1=[x for x in a[:n]]
hq2=[-x for x in a[n+n:]]
su1=sum(hq1)
su2=-sum(hq2)
mem1=[su1]
mem2=[su2]
heapify(hq1)
heapify(hq2)
for x in a[n:n+n]:
	y=heappop(hq1)
	if x>y:
		heappush(hq1,x)
		su1+=x-y
	else:
		heappush(hq1,y)
	mem1.append(su1)
for x in reversed(a[n:n+n]):
	y=-heappop(hq2)
	if x<y:
		heappush(hq2,-x)
		su2-=y-x
	else:
		heappush(hq2,-y)
	mem2.append(su2)
print(max(f-b for f,b in zip(mem1,mem2[::-1])))
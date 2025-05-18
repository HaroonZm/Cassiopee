import sys
input=sys.stdin.readline
n,m=map(int,input().split())
p=list(map(int,input().split()))
def root(x):
	if x!=parent[x]:
		x=root(parent[x])
	return x
def same (x,y):
	return root(x)==root(y)
def unite(x,y):
	rx=root(x)
	ry=root(y)
	if rank[rx]<rank[ry]:
		parent[rx]=ry
	else:
		parent[ry]=rx
		if rank[rx]==rank[ry]:
			rank[rx]+=1
parent=list(range(n))
rank=[0]*n
for i in range(m):
	x,y=map(int,input().split())
	unite(x-1,y-1)
ans=0
for i in range(n):
	if same(p[i]-1,i):
		ans+=1
print(ans)
import sys
input=sys.stdin.readline
p=[]
n,w=map(int,input().split())
for i in range(n):
	a,b=map(int,input().split())
	p.append([a/b,a,b])
p.sort(key=lambda x:-x[0])
ans=0
i=0
while w>0 and i<n:
	if w>=p[i][2]:
		ans+=p[i][1]
	else:
		ans+=p[i][1]*(w/p[i][2])
		break
	w-=p[i][2]
	i+=1
print(ans)
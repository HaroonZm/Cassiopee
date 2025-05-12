n=int(input())
a=list(map(int,input().split()))
b=[a[0]]
for i in range(n-1):
	b.append(b[-1]+a[i+1])
b.append(0)
b.sort()
cnt=0
ans=0
def c(a,b):
	u=1
	for i in range(a-b+1,a+1):
		u*=i
	for i in range(1,b+1):
		u//=i
	return u
p=b[0]
for i in range(n+1):
	if b[i]==p:
		cnt+=1
	else:
		p=b[i]
		ans+=c(cnt,2)
		cnt=1
if cnt>1:
	ans+=c(cnt,2)
print(ans)
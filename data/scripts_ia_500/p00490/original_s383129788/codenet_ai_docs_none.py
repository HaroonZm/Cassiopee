n = int(input())
a,b=map(int,input().split())
c=int(input())
ans,p=c/a,a
d=[int(input()) for _ in range(n)]
d.sort(reverse=True)
for i in range(n):
	t=(c+d[i])/(p+b)
	if t>ans:
		ans=t
		c+=d[i]
		p+=b
	else: break
print(int(ans))
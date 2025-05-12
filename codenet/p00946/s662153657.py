n,m=map(int,input().split())
a=[]
for i in range(n):
	a.append(i)
for i in range(m):
	e=int(input())
	a[e-1]=-i-1
b=[]
for i in range(n):
	b.append([a[i],i+1])
b.sort()
for i in range(n):
	print(b[i][1])
h,w,d=map(int,input().split())
field=[[]]*(h*w)
for i in range(h):
	x=list(map(int,input().split()))
	for j in range(w):
		field[x[j]-1]=[i,j]
dis=[10**20]*(h*w)
for i in range(d):
	dis[i]=0
for i in range((h*w)):
	if i>=d:
		dis[i]=dis[i-d]+abs(field[i][0]-field[i-d][0])\
		+abs(field[i][1]-field[i-d][1])
q=int(input())
for i in range(q):
	l,r=map(int,input().split())
	print(dis[r-1]-dis[l-1])
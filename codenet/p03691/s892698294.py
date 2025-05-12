n,m=map(int,input().split())
v=[[1 for i in range(n)] for i in range(n)]
for i in range(m):	
	x,y=map(int,input().split())
	x-=1
	y-=1
	if v[x][y]:
		v[x][y],v[y][x]=0,0
		for j in range(n):
			if v[x][j]==0:
				v[j][y],v[y][j]=0,0
		for j in range(n):
			if v[y][j]==0:
				v[j][x],v[x][j]=0,0
	else:
		for j in range(n):
			v[j][x],v[x][j],v[j][y],v[y][j]=0,0,0,0
print((sum(map(sum,v))-sum([v[i][i] for i in range(n)]))//2)
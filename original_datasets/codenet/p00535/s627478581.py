import queue as Q
a = list(map(int,input().split()))
b = [[] for i in range(a[0])]
c = [[] for i in range(a[0])]
qs = [None,None]
qs[0]= Q.Queue()
qs[1]= Q.Queue()
arounds=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for i in range(a[0]):
	b[i]=list(input())
	for j in range(a[1]):
		c[i].append(0)
		if b[i][j]!='.':
			b[i][j]=int(b[i][j])
for i in range(1,a[0]-1):
	for j in range(1,a[1]-1):
		for k in arounds:
			if b[i+k[0]][j+k[1]]=='.':
				c[i][j]+=1
ans=0
for i in range(a[0]):
	for j in range(a[1]):
		if b[i][j]!='.' and b[i][j]<=c[i][j]:
			b[i][j]='.'
			qs[0].put((i,j))
if qs[0].empty():
	quit()
q=0
while not qs[q].empty():
	while not qs[q].empty():
		p=qs[q].get()
		for k in arounds:
			c[p[0]+k[0]][p[1]+k[1]]+=1
			if b[p[0]+k[0]][p[1]+k[1]]!='.' and b[p[0]+k[0]][p[1]+k[1]]==c[p[0]+k[0]][p[1]+k[1]]:
				b[p[0]+k[0]][p[1]+k[1]]='.'
				qs[q^1].put((p[0]+k[0],p[1]+k[1]))
	q^=1
	ans+=1
print(ans)
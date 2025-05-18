import  heapq

n,m,s,t=map(int,raw_input().split())
src = [ tuple( map( int, raw_input().split() ) )   for i in range(m)]

nl=[ [ ] for j in range(n+1) ] 

for u,v,a,b in src:
	nl[u].append( (v,a,b) )
	nl[v].append( (u,a,b) )

#Dijkstra yen
d_y=[ float("inf") ]*(n+1)
d_y[s]=0

Q=[]
heapq.heappush(Q, (0,s) )

while Q:
	cost, u=heapq.heappop(Q)
	for v,yen,snuuk in nl[u]:
		if d_y[v] > cost+yen:
			d_y[v]=cost+yen
			heapq.heappush(Q, (d_y[v], v)  )

#Dijkstra snuuk
d_s=[ float("inf")]*(n+1)
d_s[t]=0

Q=[]
heapq.heappush(Q,(0,t) )

while Q:
	cost, u=heapq.heappop(Q)
	for v,yen,snuuk in nl[u]:
		if d_s[v] > cost+snuuk:
			d_s[v]=cost+snuuk
			heapq.heappush(Q, (d_s[v], v)  )

val=float("inf")
A=[]
for i in range(n,0,-1):
	tmp=d_y[i]+d_s[i]
	val=min(val, tmp)
	A.append(val)

for i in reversed(A):
	print 10**15-i
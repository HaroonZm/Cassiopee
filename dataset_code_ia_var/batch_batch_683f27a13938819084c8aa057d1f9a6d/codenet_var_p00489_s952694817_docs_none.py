def f():
 from heapq import heappop, heappush
 N=int(input())
 r=[0]*N
 for _ in [0]*(N*~-N//2):
  a,b,c,d=map(int,input().split())
  r[a-1]+=3*(c>d)+(c==d)
  r[b-1]+=3*(d>c)+(d==c)
 b=[[]for _ in[0]*N*3]
 for i in range(N):b[r[i]]+=[i]
 pq=[]
 for i,s in enumerate(r):heappush(pq,[-s,i])
 rank=1
 display_rank=1
 prev_score=float('inf')
 while pq:
  s,i=heappop(pq)
  if s!=prev_score:rank=display_rank
  r[i]=rank
  display_rank+=1
  prev_score=s
 print(*r,sep='\n')
f()
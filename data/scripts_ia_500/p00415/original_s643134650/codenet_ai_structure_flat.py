import heapq
N,K=map(int,input().split())
Q=[]
rest=N
need_out=N-K
out=0
table=list(map(int,input().split()))
class Info:
 def __init__(self,num,loc):
  self.num=num
  self.loc=loc
 def __lt__(self,other):
  if self.num!=other.num:
   return self.num>other.num
  return self.loc<other.loc
for loc in range(N):
 tmp=table[loc]
 heapq.heappush(Q,Info(tmp,loc))
 rest-=1
 if out+rest>=need_out:
  continue
 info=heapq.heappop(Q)
 print("%d"%(info.num),end="")
 while len(Q)>0 and Q[0].loc<=info.loc:
  heapq.heappop(Q)
print()
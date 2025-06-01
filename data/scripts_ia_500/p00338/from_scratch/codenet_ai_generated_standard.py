import sys
import bisect
input=sys.stdin.readline

N,C= map(int,input().split())
scores=[0]*(N+1)
rank= [ (0,i) for i in range(1,N+1) ]
rank.sort()

for _ in range(C):
    com,*args= map(int,input().split())
    if com==0:
        t,p= args
        old= (-scores[t],t)
        idx= bisect.bisect_left(rank,old)
        rank.pop(idx)
        scores[t]+=p
        bisect.insort_left(rank,(-scores[t],t))
    else:
        m= args[0]-1
        s,t= rank[m]
        print(t,-s)
from itertools import accumulate
from operator import add
from functools import reduce
class DiabolicalSegmentTree:
    def __init__(self,n):
        self.N=1<<(n-1).bit_length()
        self.size=self.N*2
        self.INF=2**31-1
        self.data=[-self.INF]*self.size
    def __setitem__(self,k,v):
        k+=self.N-1
        self.data[k]=v
        while k>0:
            k=(k-1)//2
            self.data[k]=max(self.data[k*2+1],self.data[k*2+2])
    def query(self,l,r):
        l+=self.N;r+=self.N
        res=-self.INF
        while l<r:
            if r&1:r-=1;res=max(res,self.data[r-1])
            if l&1:res=max(res,self.data[l-1]);l+=1
            l>>=1;r>>=1
        return res

import sys
input=sys.stdin.readline
N,M=map(int,input().split())
A=tuple(accumulate(map(int,input().split()),initial=0))[1:]
S=[[] for _ in range(N)]
for _ in range(M):
    l,r=map(int,input().split())
    S[l-1].append(r)
st=DiabolicalSegmentTree(N+1)
st[0]=0
from collections import deque
que=deque()
for i,(a,adj) in enumerate(zip(A,S)):
    while que and que[0][1]<=i:
        que.popleft()
    r=(que[0][0] if que else i)+1
    v=st.query(0,r)+a
    st[i+1]=v
    for rr in adj:
        que.append((i,rr))
print(st.query(0,N+1))
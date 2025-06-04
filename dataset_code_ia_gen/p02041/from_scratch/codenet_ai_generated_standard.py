import sys
input=sys.stdin.readline

class FenwickMax:
    def __init__(self,n):
        self.n=n
        self.data=[(0,0)]*(n+1)
    def update(self,i,val):
        while i<=self.n:
            if val[0]>self.data[i][0]:
                self.data[i]=val
            i+=i & -i
    def query(self,i):
        res=(0,0)
        while i>0:
            if self.data[i][0]>res[0]:
                res=self.data[i]
            i-=i & -i
        return res

N=int(input())
A=list(map(int,input().split()))
maxA=max(A) if A else 0
fenw=FenwickMax(maxA+1)
for x in A:
    length,sumv=fenw.query(x-1)
    length+=1
    sumv+=x
    fenw.update(x,(length,sumv))
print(fenw.query(maxA)[1])
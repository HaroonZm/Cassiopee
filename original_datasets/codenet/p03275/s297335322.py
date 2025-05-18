import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N=int(input())
    a=list(map(int,input().split()))
    
    class BIT:
        def __init__(self,n):
            self.num=n
            self.dat=[0]*(self.num+1)
            self.depth=n.bit_length()
        
        def add(self,i,x):
            i+=1
            while i<=self.num:
                self.dat[i]+=x
                i+=i&-i
        
        def sum(self,i):
            i+=1
            s=0
            while i>0:
                s+=self.dat[i]
                i-=i&-i
            return s
        
        def lower_bound(self,x):
            sum_=0
            pos=0
            for i in range(self.depth,-1,-1):
                k=pos+(1<<i)
                if k<=self.num and sum_+self.dat[k]<x:
                    sum_+=self.dat[k]
                    pos+=1<<i
            return pos, sum_
    
    def nibutan(ok,ng):
        while abs(ok-ng) > 1:
            mid = (ok + ng) // 2
            if solve(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    def solve(mid):
        aa=[1 if x>=mid else -1 for x in a]
        b=BIT(N*2+1)
        c=0
        s=N
        b.add(s,1)
        for x in aa:
            s+=x
            c+=b.sum(s)
            b.add(s,1)
        return c>=-(-N*(N+1)//2//2)
    
    print(nibutan(1,10**9+1))

if __name__ == '__main__':
    main()
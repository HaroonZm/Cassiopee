class ABSsegtree: # 必要な配列の長さN,単位元ie,関数(2項演算)func,を渡す    
    def __init__(self,N,ie,func):
        self.func=func
        self.getLEN=1 # Length of list
        while self.getLEN<N:
            self.getLEN*=2
        self.getsize=self.getLEN*2 # =len(ST)
        self.getLIN=self.getsize-self.getLEN # internal nodes without ST[0]
        self.ST=[ie]*self.getsize

    def update(self,i,x): # i(0-index)にxをいれる
        i+=self.getLIN
        self.ST[i]=x
        while i>1:
            i//=2
            self.ST[i]=self.func(self.ST[2*i],self.ST[2*i+1])
    
    def get_interval(self,a,b): # [a,b)での最小値を求めたい
        a+=self.getLIN
        b+=self.getLIN
        ret=self.func(self.ST[a],self.ST[b-1])
        while a+1<b: # 階層ごとに見る
            if a%2==1:
                ret=self.func(self.ST[a],ret)
                a+=1
            a//=2
            if b%2==1:
                ret=self.func(self.ST[b-1],ret)
            b//=2
        if a==b:
            pass
        else:
            ret=self.func(ret,self.ST[a])
        return ret
      
import fractions

N=int(input())
A=[int(a) for a in input().split()]

ins=ABSsegtree(N,0,fractions.gcd)
for i,a in enumerate(A):
  ins.update(i,a)
ans=0
for i,a in enumerate(A):
  ins.update(i,0)
  ans=max(ans,ins.get_interval(0,N))
  ins.update(i,a)
print(ans)
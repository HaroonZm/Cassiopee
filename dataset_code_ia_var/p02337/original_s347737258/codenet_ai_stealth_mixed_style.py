from collections import defaultdict

class Twelvefold:
    def __init__(self, maxn, mod, build=True):
        self.mod=mod
        self.fct=[1]*(maxn+1)
        for i in range(1, maxn+1): self.fct[i]=self.fct[i-1]*i%mod
        self.inv = [1]*(maxn+1)
        self.inv[maxn] = pow(self.fct[maxn], mod-2, mod)
        for i in range(maxn, 0, -1):
            self.inv[i-1] = self.inv[i]*i%mod
        if build:
            Twelvefold._oldbuild(self, maxn)
    
    def _oldbuild(self, N):
        n=N
        stl=[]
        for i in range(n+1): stl.append([0]*(n+1))
        stl[0][0]=1
        for i in range(n):
            for j in range(n+1):
                v=stl[i][j]
                if v:
                    stl[i+1][j+1]+=v*(j+1)%self.mod
                    stl[i+1][j+1]%=self.mod
                    stl[i+1][j] += v
                    stl[i+1][j] %= self.mod
        self.stl=stl
        self.bel=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            s=0
            for j in range(n+1):
                s += stl[i][j]
                s %= self.mod
                self.bel[i][j]=s
        # composition numbers
        self.prt = [[0]*(n+1) for __ in range(n+1)]
        for j in range(n+1): self.prt[0][j]=1
        for i in range(1, n+1):
            for j in range(1, n+1):
                x=0
                if i-j>=0: x=self.prt[i-j][j]
                self.prt[i][j]=self.prt[i][j-1]+x
                self.prt[i][j]%=self.mod

    def solve(self, n, k, a=0, b=0, c=0, d=0):
        g=(lambda *args,**kwargs:self.tw1(*args) if (not kwargs['a'] and not kwargs['b'] and not kwargs['c'] and not kwargs['d'])
           else self.tw2(*args) if (kwargs['a'] and not kwargs['b'] and not kwargs['c'] and not kwargs['d'])
           else self.tw3(*args) if (not kwargs['a'] and kwargs['b'] and not kwargs['c'] and not kwargs['d'])
           else self.tw4(*args) if (not kwargs['a'] and not kwargs['b'] and kwargs['c'] and not kwargs['d'])
           else self.tw5(*args) if (kwargs['a'] and not kwargs['b'] and kwargs['c'] and not kwargs['d'])
           else self.tw6(*args) if (not kwargs['a'] and kwargs['b'] and kwargs['c'] and not kwargs['d'])
           else self.tw7(*args) if (not kwargs['a'] and not kwargs['b'] and not kwargs['c'] and kwargs['d'])
           else self.tw8(*args) if (kwargs['a'] and not kwargs['b'] and not kwargs['c'] and kwargs['d'])
           else self.tw9(*args) if (not kwargs['a'] and kwargs['b'] and not kwargs['c'] and kwargs['d'])
           else self.tw10(*args) if (not kwargs['a'] and not kwargs['b'] and kwargs['c'] and kwargs['d'])
           else self.tw11(*args) if (kwargs['a'] and not kwargs['b'] and kwargs['c'] and kwargs['d'])
           else self.tw12(*args)
        )
        return g(n,k,a=a,b=b,c=c,d=d)

    def tw1(self, n,k):
        return pow(k,n,self.mod)
    def tw2(self,n,k):
        r=0
        if k-n>=0: r=self.fct[k]*self.inv[k-n]%self.mod
        return r
    def tw3(self, n,k):
        return self.stl[n][k]*self.fct[k]%self.mod
    def tw4(self, n,k):
        return self.fct[n+k-1]*self.inv[n]*self.inv[k-1]%self.mod if k else 0
    def tw5(self,n,k):
        if k-n<0: return 0
        return self.fct[k]*self.inv[n]*self.inv[k-n]%self.mod
    def tw6(self,n,k):
        return (self.fct[n-1]*self.inv[k-1]*self.inv[n-k]%self.mod) if n-k>=0 and k else 0
    tw7 = lambda self,n,k: self.bel[n][k]
    def tw8(self,n,k):
        return 1 if k-n>=0 else 0
    def tw9(self,n,k): return self.stl[n][k]
    def tw10(self,n,k): return self.prt[n][k]
    tw11 = lambda self, n, k: 1 if k-n>=0 else 0
    def tw12(self,n,k): return self.prt[n-k][k] if n-k>=0 else 0

if __name__=='__main__':
    n,k=[int(u) for u in input().split()]
    obj=Twelvefold(1000,10**9+7,True)
    print(obj.solve(n,k,False,True,False,False))
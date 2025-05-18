class RMQ:
    inf = 0
    def __init__(self,n_):
        self.n_ = n_
        self.n = 1
        while self.n < n_: self.n*=2
        self.st = [self.inf]*(2*self.n-1)
    
    def update(self,k,x):
        k+=(self.n-1)
        self.st[k] = x
        while k >0:
            k = (k-1)//2
            self.st[k] = max(self.st[2*k+1],self.st[2*k+2])

    def search(self,a,b,k,l,r):
        if r<=a or b<=l :return self.inf
        if a<=l and r<=b:return self.st[k]
        L = self.search(a,b,k*2+1,l,(l+r)//2)
        R = self.search(a,b,k*2+2,(l+r)//2,r)
        return max(L,R)

    def query(self,a,b):
        return self.search(a,b,0,0,self.n)

n = int(input())
x = list(map(int,input().split()))
rmq = RMQ(n+1)
for i in x:
    res = rmq.query(1,i)
    rmq.update(i,i+res)
print (sum(x)-rmq.query(1,n+1))
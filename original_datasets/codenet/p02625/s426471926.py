class Combination():
    def __init__(self, n, mod):
        self.n = n
        self.mod = mod
        self.fact = self.make_fact(n)
        self.fact_inv = self.make_fact_inv(n)
    def make_fact(self, n):#0~nの階乗を求める
        res = [1]*(n+1)
        for i in range(1, n+1):
            res[i] = res[i-1]*i%self.mod
        return res
    def make_fact_inv(self, n):#0~nの階乗のmodに関する逆元を求める
        fact_inv = [1]*(n+1)
        fact_inv[n] = pow(self.fact[n], self.mod-2, self.mod)#フェルマーの小定理
        for i in range(n, 0, -1):
            fact_inv[i-1] = fact_inv[i]*i%self.mod
        return fact_inv
    def c(self, m, k):
        return self.fact[m]*self.fact_inv[k]*self.fact_inv[m-k]%self.mod
    def p(self,m,k):
        return self.fact[m]*self.fact_inv[m-k] %self.mod
mod = 10**9+7

n,m=map(int,input().split())
com = Combination(m,mod)

ans=0
for i in range(n+1):
    ans += com.c(n,i) * (-1)**i * com.p(m,i) * (com.p(m-i,n-i))**2
    ans %= mod
    
print(ans)
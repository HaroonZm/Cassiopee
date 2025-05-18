class BIT: #0-indexed
    __slots__ = ["size", "tree","depth","n0"]
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)
        self.depth = n.bit_length()
        self.n0 = 1<<self.depth

    def get_sum(self, i): #a_0 + ... + a_{i} #閉区間
        s = 0; i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def range_sum(self,l,r): #a_l + ... + a_r 閉区間
        return self.get_sum(r) - self.get_sum(l-1) 

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def bisect_left(self,w):
        #和が w 以上になる最小の index
        #w が存在しない場合 self.size を返す
        if w <= 0: return 0
        x,k = 0,self.n0
        for _ in range(self.depth):
            k >>= 1
            if x+k <= self.size and self.tree[x+k] < w:
                w -= self.tree[x+k]
                x += k
        return x

# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n,k = map(int,readline().split())
*p, = map(int,readline().split())

b = BIT(n)
num = BIT(n)
MOD = 998244353
inv2 = (MOD+1)//2
for i in range(k):
    b.add(p[i]-1,inv2)
    num.add(p[i]-1,1)

ans = k*(k-1)//2%MOD*inv2%MOD

prob = (k-1)*pow(k,MOD-2,MOD)%MOD #(k-1/k)
pinv = pow(prob,MOD-2,MOD)
val = pinv*inv2%MOD #(k-1)/k/2: これを bit に足していく
rate = prob #倍率
for j in range(k,n):
    # p_i < p_j
    pj = p[j]-1
    v = b.get_sum(pj)
    ans += v*rate%MOD
    ans %= MOD

    # p_i > p_j
    w =  b.get_sum(n-1)-v
    ans += (j - num.get_sum(pj)) - w*rate%MOD
    ans %= MOD
    
    b.add(pj,val)
    num.add(pj,1)
    val = val*pinv%MOD
    rate = rate*prob%MOD

print(ans%MOD)
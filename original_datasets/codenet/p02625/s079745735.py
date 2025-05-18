import sys
input = sys.stdin.readline

# N = 4

# for M in range(N, N+5):
#     P = list(permutations(range(M),N))
#     #print(P)
#     ans = 0
#     for A in P:
#         ok = True
#         for i, a in enumerate(list(A)):
#             if i == a:
#                 ok = False
#                 break
#         if ok:
#             ans += 1
#     print(ans)

mod = 10**9+7
N, M = map(int, input().split())

# コンビネーション
mod = 10**9+7
def cmb(n, r, mod=mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

NN = 6*10**5 # 使うデータによって変える
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, NN + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

# a(n) = sum((-1)^i*binomial(3,i)*(n-i)!/(n-3)!,i=0..3).

ans = 0
for k in range(N+1):
    ans = (ans + (-1)**k * cmb(N, k)*g1[M-k]*g2[M-N] ) % mod
print(ans*g1[M]*g2[M-N]%mod)
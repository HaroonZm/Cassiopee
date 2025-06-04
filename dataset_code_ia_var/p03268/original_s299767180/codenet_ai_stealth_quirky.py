from sys import stdin as __S; __I = __S.readline

N, K = map(int, __I().split())

__A = divmod(N, K)

___ = lambda x: __A[0]+(1 if (x!=0 and x<=__A[1])or(x==0 and __A[1]==K) else 0)

Ω, i = 0, 0

while i<K:
    α=i
    β=(-i)%K
    γ=(-i)%K
    if not (β+γ)%K:
        Ω+=___(α)*___(β)*___(γ)
    i+=1

print(Ω)
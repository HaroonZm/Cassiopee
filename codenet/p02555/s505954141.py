s = int(input())

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7
N = 3000
g1 = [1, 1]
g2 = [1, 1]
inverse = [0, 1]

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

ans = 0
for i in range(1, 2000):
    if s-3*i < 0:
        break

    ans += cmb(s-3*i+i-1, i-1, mod)
    ans %= mod

print(ans)
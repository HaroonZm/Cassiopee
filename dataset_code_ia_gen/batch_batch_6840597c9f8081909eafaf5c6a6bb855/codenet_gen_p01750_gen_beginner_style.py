mod = 10**9 + 7

d = int(input())
l = [int(input()) for _ in range(d)]
s = int(input())

# dp[i][j]: nombre de façons de choisir x_1..x_i avec somme j, chaque x_i <= l[i-1]
max_s = sum(l)
dp = [0]*(max_s+1)
dp[0] = 1

for i in range(d):
    ndp = [0]*(max_s+1)
    prefix = [0]*(max_s+2)
    for j in range(max_s+1):
        prefix[j+1] = (prefix[j] + dp[j]) % mod
    for j in range(max_s+1):
        left = j - l[i]
        if left < 0:
            left = 0
        ndp[j] = (prefix[j+1] - prefix[left]) % mod
    dp = ndp

# dp[j] = nombre de points entiers dans [0,l_1]x...x[0,l_d] avec somme j
# On veut somme_{x1+...+xd <= s} dp[x1+...+xd] * volume des petits cubes (ici volume unitaire)
# En fait dp est déja le nombre de points. Le problème demande V volumen (la partie continue)
# La valeur cherchée est d! * volume des points avec somme <= s.

# On utilise la relation donnée: d! V est un entier et égale à somme_{k=0}^{s} f(k)
# avec f(k)= nombre des points à somme k multiplié par une certaine combinatoire.

# En fait, d! V = somme_{k=0}^s comb(k + d -1, d -1) * nombre de points à somme k

# Il faut calculer comb(k + d, d) rapidement

fact = [1]*(d+max_s+1)
for i in range(1,d+max_s+1):
    fact[i] = fact[i-1]*i % mod

invfact = [1]*(d+max_s+1)
invfact[-1] = pow(fact[-1], mod-2, mod)
for i in range(d+max_s-1, -1, -1):
    invfact[i] = invfact[i+1]*(i+1) % mod

def comb(n,r):
    if r>n or r<0:
        return 0
    return fact[n]*invfact[r]%mod*invfact[n-r]%mod

ans = 0
for k in range(s+1):
    val = dp[k]*comb(k+d-1,d-1) % mod
    ans = (ans + val) % mod

print(ans)
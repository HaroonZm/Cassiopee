# Lecture des entrées
entrees = input().split()
r1 = int(entrees[0])
c1 = int(entrees[1])
r2 = int(entrees[2])
c2 = int(entrees[3])

mod = 10**9 + 7

# Pré-calcul des factorielles et inverse modulaire
nombre = r2 + c2 + 10
fac = [1] * (nombre + 1)
inv = [1] * (nombre + 1)

for i in range(1, nombre + 1):
    fac[i] = fac[i-1] * i % mod

for i in range(0, nombre + 1):
    inv[i] = pow(fac[i], mod-2, mod)

def combinaison(n, r):
    return fac[n] * inv[n-r] % mod * inv[r] % mod

def fonction_g(x, y):
    return combinaison(x + y, y)

# Calcul du résultat
resultat = fonction_g(r2+1, c2+1)
resultat -= fonction_g(r2+1, c1)
resultat -= fonction_g(r1, c2+1)
resultat += fonction_g(r1, c1)
resultat = resultat % mod

print(resultat)
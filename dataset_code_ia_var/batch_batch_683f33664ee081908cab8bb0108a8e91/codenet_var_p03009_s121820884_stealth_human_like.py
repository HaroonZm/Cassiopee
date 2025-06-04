import sys

# Perso, je préfère garder range, mais bon, on garde aussi la compatibilité py2 ici...
range = xrange  
input = raw_input

mod = 10**9 + 7

# on récupère les entrées, classique...
n, h, d = map(int, input().split())

# ça fait peut-être un peu grand mais on ne sait jamais
big = 10 ** 6 + 10

# génération des factorielles, mais on pourrait juste prendre jusqu'à n, pas grave
fac = [1]
while len(fac) < big:
    fac.append((fac[-1] * len(fac)) % mod)

# cumul des factorielles, pas certain que ça soit le plus efficace...
cumfac = [0]
for ff in fac:
    cumfac.append((cumfac[-1] + ff) % mod)

DP = [0] * (h + 1)
DP[0] = fac[n]  # de base, y'a aucune contrainte à 0, c'est la factorielle

# donc là, on prend cumfac entre n+1 et 1, étrange mais ok
multi = cumfac[n + 1] - cumfac[1]
s = 0
for i in range(1, h):
    s += DP[i - 1]
    if i - d - 1 >= 0:
        s -= DP[i - d - 1]
    s %= mod  # attention au modulo
    DP[i] = (s * multi) % mod  # un peu peu verbeux, faudrait commenter ce calcul

# traitement particulier pour la fin
DP[h] = sum(DP[max(0, h - d):h]) % mod

# affichage de la solution, je trouve print sans parenthèses moche mais bon py2 hein
print DP[-1]
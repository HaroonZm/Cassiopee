MOD = 10**9 + 7

# On doit compter le nombre de façons de répartir N cookies en D jours,
# en mangeant strictement moins que X cookies par jour.
# Autrement dit, pour chaque jour i (1 ≤ i ≤ D), on choisit un entier a_i avec 1 ≤ a_i < X,
# tel que la somme des a_i soit N.

# Formulation mathématique:
# Nous cherchons le nombre de solutions (a_1, ..., a_D) en entiers, telles que:
# sum a_i = N, avec 1 ≤ a_i < X.
# C'est un problème classique de combinaison avec contraintes sur les parts,
# et on peut utiliser la fonction génératrice:
# f(t) = (t + t^2 + ... + t^{X-1})^D = (t*(1 - t^{X-1})/(1 - t))^D.

# Le coefficient de t^N dans f(t) nous donne le nombre souhaité.

# Problème:
# - D peut être très grand (jusqu'à 10^{12}), donc on ne peut pas faire de DP direct.
# - N et X sont petits (≤ 2000).
# - Nous voulons calculer coef de t^N dans f(t).

# Approche:
# On note g(t) = (1 - t^{X-1}) / (1 - t) = 1 + t + ... + t^{X-2}
# donc f(t) = (t * g(t))^D = t^D * g(t)^D

# Le coefficient recherché est coeff de t^N dans t^D * g(t)^D
# c'est équivalent au coeff de t^{N - D} dans g(t)^D

# On définit:
# h(t) = g(t) = sum_{j=0}^{X-2} t^j
# On veut coeff de t^{N - D} dans h(t)^D

# Remarque:
# - N-D peut être négatif => alors nombre de façons = 0 (impossible à répartir avec au moins 1 cookie par jour)
# - h(t) a degré X-2, donc h(t)^D a degré D*(X-2)
# - Si N-D > D*(X-2), alors nombre de façons = 0

# Taille maximale de N est 2000, donc N-D ≤ 2000, donc on peut limiter à kmax = N-D ≤ 2000.

# Donc le problème se résume à:
# calculer coef de t^{K} dans h(t)^D avec K = N-D et h(t) = sum_{j=0}^{X-2} t^j

# On peut modéliser cette puissance par exponentiation rapide sous forme de polynômes modulo t^{k_max+1}

# Résumé de l'algorithme:
# 1. lire chaque triplet (N,D,X)
# 2. si (N,D,X) = (0,0,0) -> fin
# 3. calculer K = N-D,
#    si K < 0 ou K > D*(X-2) => print 0
# 4. calculer h(t) = [1]* (X-1) termes (coef de 1 pour t^0..t^{X-2})
# 5. calculer h(t)^D modulo t^{K+1} (on ne garde que puissances ≤ K)
#    via exponentiation rapide de polynômes
# 6. retourner coef de t^K dans le résultat

# Remarque sur la multiplication:
# degré max = K ≤ 2000,
# donc multiplication naïve O(K^2) est OK car max 100 datasets.

def poly_mul(a, b, k_max):
    """Multiplie deux polynômes a et b modulo t^{k_max+1}"""
    res = [0] * (k_max + 1)
    for i in range(len(a)):
        ai = a[i]
        if ai == 0:
            continue
        for j in range(len(b)):
            if i + j > k_max:
                break
            res[i + j] = (res[i + j] + ai * b[j]) % MOD
    return res

def poly_pow(base, exponent, k_max):
    """Calcule base^exponent modulo t^{k_max+1} par exponentiation rapide"""
    result = [1] + [0]*k_max  # polynôme 1
    cur = base
    e = exponent
    while e > 0:
        if e & 1:
            result = poly_mul(result, cur, k_max)
        cur = poly_mul(cur, cur, k_max)
        e >>=1
    return result

import sys

for line in sys.stdin:
    if line.strip() == '':
        continue
    N,D,X = map(int,line.strip().split())
    if N == 0 and D == 0 and X ==0:
        break
    K = N - D
    # si impossible
    if K <0 or K > D*(X-2):
        print(0)
        continue
    # construire h(t) = 1 + t + t^2 + ... + t^{X-2}
    # coef h de longueur X-1
    h = [1]*(X-1)

    # calcul h^D mod t^{K+1}
    poly = poly_pow(h, D, K)
    # coef de t^K dans h^D correspond coef t^N dans f(t)
    print(poly[K] % MOD)
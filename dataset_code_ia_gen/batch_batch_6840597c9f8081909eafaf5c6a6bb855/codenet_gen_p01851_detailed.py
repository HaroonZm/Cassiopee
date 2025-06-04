import sys
sys.setrecursionlimit(10**7)

MOD = 10**9 + 7

# LRU cache comme mémorisation pour accélérer les appels récursifs
from functools import lru_cache

"""
Problem:
Given A, B, C matches where Team X wins A times, Team Y wins B times, and C draws.
Total scores: Sx for X, Sy for Y.
Each match score is (x_i, y_i), x_i,y_i >= 0 integers:
- For X win match: x_i > y_i
- For Y win match: x_i < y_i
- For draw: x_i == y_i
The sum over matches of x_i = Sx, sum of y_i = Sy.
Count the number of sequences of such scores respecting the order of matches,
mod 10^9+7.
"""

# On pose dp pour chaque catégorie :
# Pour chaque catégorie (X_win, Y_win, draw) avec n matchs,
# on veut connaître le nombre de façons d'attribuer les scores (x_i,y_i) aux n matchs,
# totalisant (x_total,y_total) et respectant le critère de victoire/draw.

# L'idée clef est que puisque on doit compter les combinaisons ordonnées,
# et chaque match est indépendant du score des autres à part par la somme totale,
# on peut factoriser en convolutionnations des distributions des scores par match.

# On définit:
# fX[i][sx][sy]: nombre de façons de faire i matchs gagnés par X avec total sx, sy
# fY[i][sx][sy]: comme ci-dessus mais Y gagne
# fD[i][sx][sy]: comme ci-dessus mais match nul

# Ces tableaux sont énormes pour les contraintes données (jusqu'à 10^6),
# donc approche DP classique impossible.

# Observons les conditions sur les scores dans un match:

# - Pour un match gagné par X : x > y >= 0
#    donc (x,y) satisfaisant x > y >= 0.

# - Pour un match gagné par Y : y > x >= 0

# - Pour un match nul: x == y >= 0

# Nous devons compter le nombre de façons de répartir les points par match,
# totalisant un certain total de points, avec le symbole correspondante.

# Comment procéder efficacement ?

# 1) On note que chaque match d'une catégorie est indépendant et identique.

# 2) Le nombre de façons pour faire n matchs dans une catégorie est la convolution n fois
#    de la distribution des scores possibles dans un match de cette catégorie.

# 3) Si on note la fonction génératrice pour les scores (x,y) d'un match de cette catégorie
#    comme P(x,y) = sum over all possible (x,y) score configurations de z^x * w^y,
#    alors la fonction génératrice des scores de n matchs est P(z,w)^n.

# 4) on veut la somme des coefficients [z^{Sx_i} w^{Sy_i}] dans P(z,w)^n

# Le problème devient:
# On veut calculer le coefficient de z^{s} w^{t} dans P(z,w)^n.

# Or A, B, C sont petits pour les exemples test mais jusqu'à 10^6 dans l'entrée.

# On va décomposer donc le problème en la somme des contributions des 3 catégories.

# Pour la combinaison multinomial, le nombre total de façons est :
# somme sur toutes décompositions:
# sX = sX1 + sX2 + sX3 = Sx
# sY = sY1 + sY2 + sY3 = Sy
# avec:
# sX1,sY1 = total score de A matchs gagnés par X,
# sX2,sY2 = total score de B matchs gagnés par Y,
# sX3,sY3 = total score de C matchs nuls.

# On doit calculer:
# ways = sum_{sX1,sY1,sX2,sY2,sX3,sY3}
#        fX(A,sX1,sY1) * fY(B,sX2,sY2) * fD(C,sX3,sY3)
#  avec contraintes sX1+sX2+sX3 = Sx et sY1+sY2+sY3 = Sy

# Pour seulement les catégories individuelles,
# nous devons calculer fX, fY, fD.

# Pour un match nul (draw):
# possible scores = (k,k), k >= 0
# Pour C matchs nuls, somme x = sum k_i = s,
# somme y = sum k_i = s (car x=y)
# donc sX3 = sY3 = total points sur ces matchs.

# Le nombre de façons pour C matchs nuls totalisant s points chacun (car sum x = sum y = s):
# Combinaison de mettre le total s parmi C matchs sans restriction sur les k_i >= 0.
# Nombre de solutions integres de k_1+...+k_C = s avec k_i >= 0 :
# C-sballs problem = comb(s+C-1, C-1)

# Donc fD(C, sX3, sY3) = 0 si sX3 != sY3,
# sinon comb(sX3+C-1, C-1).

# Pour un match gagné par X (score x > y >= 0), chaque match a x>y.

# Pour une seule partie gagnée par X:
# Les scores possibles (a,b) sont b < a, a,b >=0

# Le nombre de possibilités pour un match gagné par X avec score (a,b) est 1 par choix (a,b) satisfaisant a > b >=0.

# Pour A matchs gagnés par X:
# Nous cherchons le nombre de façons de décomposer Sx1 points pour X et Sy1 points pour Y
# dans A couples (a_i,b_i), a_i > b_i.

# Cela revient à compter le nombre d'entiers non négatifs A-tuples (a_i,b_i) avec a_i > b_i,
# somme a_i = Sx1, somme b_i = Sy1.

# Cela peut être transformé :
# posons d_i = a_i - b_i, d_i >= 1 (car a_i > b_i ; donc d_i ≥ 1)
# et b_i >= 0
# somme a_i = sum b_i + sum d_i = Sy1 + sum d_i = Sx1
# donc sum d_i = Sx1 - Sy1  (noté D = Sx1 - Sy1)

# Les conditions deviennent:
# - d_i >= 1
# - b_i >= 0
# - sum d_i = D
# - sum b_i = Sy1

# Le nombre de façons de choisir (d_i) avec d_i >=1 et sum d_i = D est :
# combinaison pour la somme de A entiers strictement positifs = comb(D-1, A-1) si D≥A

# Le nombre de façons de choisir (b_i) avec b_i >= 0 et sum b_i = Sy1 est
# comb(Sy1 + A -1, A-1)

# Par indépendance et multiplication des choix:
# nombre total façons = comb(D-1, A-1)*comb(Sy1 + A -1, A-1) si D≥A, sinon 0

# Condition D = Sx1 - Sy1 ≥ A ? sinon 0.

# De même pour Y gagnant, on échange les rôles:
# (a_i, b_i) avec b_i > a_i
# posons d_i = b_i - a_i ≥ 1
# sum b_i = Sy2, sum a_i = Sx2
# sum d_i = Sy2 - Sx2 = D_Y

# nombre façons = comb(D_Y -1, B -1)*comb(Sx2 + B -1, B -1) if D_Y ≥ B else 0

# Maintenant, on a des expressions fermées de fX, fY, fD.

# Enfin, on doit calculer:

# sum_{sX1,sY1,sX2,sY2,sX3}
# fX(A,sX1,sY1)*fY(B,sX2,sY2)*fD(C,sX3,sY3)
# avec :
# sX1+sX2+sX3 = Sx
# sY1+sY2+sY3 = Sy
# ici sX3 == sY3 (pour draw)

# On va itérer sX3 de 0 à min(Sx,Sy),
# et pour ce sX3 = sY3, on a fD(C,sX3,sY3)=comb(sX3+C-1,C-1).

# Ensuite sX - sX3 = sX12, sY - sY3 = sY12

# On doit calculer :
# sum_{sX1=0..sX12} sum_{sY1=0..sY12}
# fX(A,sX1,sY1)* fY(B, sX12 - sX1, sY12 - sY1)

# Pour chaque fX,fY, on met les contraintes D_X=sX1 - sY1 ≥ A
#                                     D_Y=sY2 - sX2 ≥ B
# sinon 0

# Pour les performances, on fait la somme double en itérant sur sX1,sY1.

# Utilisation de la mémoire pré-calculée des combinaisons.

# Toutes les combinaisons nécessaires seront jusqu'à max = 1_000_000 + maximum du A,B,C.

# Fonction pour factorial et inverse modulo et combinaisons modulaire

MAX = 1000000 + 5000  # marge
fact = [1]*(MAX+1)
invfact = [1]*(MAX+1)

def modinv(a, m=MOD):
    return pow(a,m-2,m)

def precompute():
    for i in range(1,MAX+1):
        fact[i] = fact[i-1]*i % MOD
    invfact[MAX] = modinv(fact[MAX], MOD)
    for i in range(MAX-1,-1,-1):
        invfact[i] = invfact[i+1]*(i+1)%MOD

def comb(n,k):
    if n<0 or k<0 or k>n:
        return 0
    return fact[n]*invfact[k]%MOD*invfact[n-k]%MOD

def ways_x_win(A, sX1, sY1):
    # D = sX1 - sY1
    D = sX1 - sY1
    if A == 0:
        return 1 if sX1 == 0 and sY1 == 0 else 0
    if D < A or sY1 < 0:
        return 0
    # comb(D-1,A-1)*comb(sY1+A-1,A-1)
    return comb(D-1, A-1)*comb(sY1 + A -1, A-1)%MOD

def ways_y_win(B, sX2, sY2):
    D = sY2 - sX2
    if B == 0:
        return 1 if sX2 == 0 and sY2 == 0 else 0
    if D < B or sX2 < 0:
        return 0
    return comb(D-1,B-1)*comb(sX2 + B -1,B-1)%MOD

def ways_draw(C, s):
    # nombre de façons = comb(s + C -1, C -1)
    if C == 0:
        return 1 if s == 0 else 0
    if s < 0:
        return 0
    return comb(s + C -1, C -1)

def solve_one_case(A,B,C,Sx,Sy):
    # On itère sur sX3 == sY3 = s_draw_points
    # total Sx, Sy données
    # On teste s_draw_points de 0 à min(Sx,Sy)
    # Pour chaque s_draw_points:
    # on calcule fD, puis les combinaisons fX et fY avec restes.
    res = 0
    max_draw_points = min(Sx,Sy)
    for s_draw_points in range(max_draw_points+1):
        ways_draw_part = ways_draw(C, s_draw_points)
        if ways_draw_part == 0:
            continue
        Sx12 = Sx - s_draw_points
        Sy12 = Sy - s_draw_points
        # On veut sum_{sX1=0..Sx12} sum_{sY1=0..Sy12} ways_x_win(A,sX1,sY1)*ways_y_win(B,Sx12 - sX1, Sy12 - sY1)
        # Optimisation: on peut parcourir sX1 in [max(0,Sx12-B*0): min(Sx12,Sx12)]
        # mais pas trivial -> on fait brute force sur les limites raisonnables

        # Par contraintes des combinaisons, nous pouvons limiter les itérations:
        # Pour ways_x_win non 0:
        # D_X = sX1 - sY1 >= A and sY1 >=0
        # Pour ways_y_win non 0:
        # D_Y = (Sy12 - sY1) - (Sx12 - sX1) >= B 
        # ==> (Sy12 - sY1) - (Sx12 - sX1) >= B
        # ==> sX1 - sY1 >= B - (Sy12 - Sx12) = B - (Sy12 - Sx12)

        # On a donc deux contraintes sur sX1 - sY1:
        # sX1 - sY1 >= A
        # sX1 - sY1 >= B - (Sy12 - Sx12)
        # donc sX1 - sY1 >= max(A, B - (Sy12 - Sx12)) = M

        M = max(A, B - (Sy12 - Sx12))

        # On limite les itérations sur sY1 de 0..Sy12
        # et pour chaque sY1, on cherche sX1 in [max(0,M+sY1), Sx12]

        # Pour réduire la double boucle, on échange l'ordre:
        # pour sY1 in [0,Sy12]
        # sX1 min = max(0, M + sY1)
        # sX1 max = Sx12

        total = 0
        for sY1 in range(Sy12+1):
            min_sX1 = max(0,M + sY1)
            if min_sX1 > Sx12:
                continue
            max_sX1 = Sx12
            # somme sur sX1 de ways_x_win * ways_y_win
            # ways_x_win(A, sX1, sY1)
            # ways_y_win(B, Sx12 - sX1, Sy12 - sY1)

            # On calculera cette somme brut mais il pourrait être lent.

            # On cache les valeurs pour vitesse
            for sX1 in range(min_sX1, max_sX1+1):
                wx = ways_x_win(A,sX1,sY1)
                wy = ways_y_win(B, Sx12 - sX1, Sy12 - sY1)
                val = wx*wy % MOD
                total = (total + val) % MOD

        ways_total = ways_draw_part*total % MOD
        res = (res + ways_total) % MOD
    return res

def main():
    precompute()
    for line in sys.stdin:
        if not line.strip():
            continue
        A,B,C,Sx,Sy = map(int,line.split())
        if A == 0 and B == 0 and C == 0 and Sx == 0 and Sy ==0:
            break
        ans = solve_one_case(A,B,C,Sx,Sy)
        print(ans)

if __name__ == '__main__':
    main()
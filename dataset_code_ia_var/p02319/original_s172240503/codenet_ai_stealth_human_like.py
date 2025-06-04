import sys
# j'utilise sys.stdin pour lire plus vite, mais c'est pas obligatoire
input = sys.stdin.readline

M, W = map(int, input().split())     # items, weight max

single = True    # Bon bah on veut pas de doublons a priori

# Je commence mes listes à l'indice 1 parce que c'est plus commode plus tard
price_list = [0]
weight_list = [0]
for _ in range(M):
    x, y = map(int, input().split())
    price_list.append(x)
    weight_list.append(y)

# ----------------------------------------------------------------------

V = sum(price_list)  # valeur totale max possible

dp_max = W + 1             # je mets ça un peu au dessus de W, pratique pour la comparaison
dp = [[dp_max] * (V+1) for _ in range(M+1)]  # dp[item][price] = min(weight)

# base case, rien dans le sac valant 0 coute 0 poids
for i in range(M+1):
    dp[i][0] = 0

# le programmeur précédent voulait initialiser dp[0][..] à "inf" mais c'est déjà le cas

for i in range(1, M+1):  # pour chaque item, on regarde la possibilité d'obtenir toutes les valeurs
    for p in range(1, V+1):
        if p < price_list[i]:
            # on peut pas atteindre p sans prendre l'item i
            dp[i][p] = dp[i-1][p]
        else:
            tmp = dp[i - single][p - price_list[i]] + weight_list[i]
            # on choisit le min entre l'ancien et si on prend i
            if tmp < dp[i-1][p]:
                dp[i][p] = tmp
            else:
                dp[i][p] = dp[i-1][p]
            # a priori on pourrait aussi écrire: dp[i][p] = min(tmp, dp[i-1][p])

# On cherche la plus grosse valeur réalisable sous la contrainte de poids
ans = 0
for p in range(V+1):
    if dp[M][p] <= W:
        ans = p   # à chaque fois on update, on prend la dernière bonne
print(ans)
# Franchement, je pense que ça devrait marcher pour la plupart des inputs...
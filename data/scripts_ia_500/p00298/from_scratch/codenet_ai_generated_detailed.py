import sys
sys.setrecursionlimit(10**7)

# On utilise une programmation dynamique pour résoudre ce problème.
# Idée générale :
# Chaque force représente une pile verticale de力持ち.
# On veut minimiser le nombre de piles (personnes marchant au sol).
#
# Approche :
# 1. On traite les 力持ち de gauche à droite.
# 2. Pour chaque position i, on calcule toutes les piles possibles qui peuvent être formées avec les 力持ち i..j empilés en une seule pile,
#    si c'est possible avec les contraintes de capacité.
# 3. On utilise une DP où dp[i] = nombre minimal de piles nécessaires pour les 力持ち de 1 à i.
# 4. Pour calculer dp[i], on essaie tous les j < i tels que les 力持ち de j+1 à i peuvent former une pile valide.
#    alors dp[i] = min(dp[i], dp[j] + 1)
#
# Détail de la validation d'une pile valide (de i à j) :
# - Les 力持ち sont empilés verticalement du bas (i) vers le haut (j).
# - Chaque 力持ち au dessous doit supporter le poids total de ceux au dessus (poids cumulés).
# - On vérifie que pour chaque 力持ち k dans [i..j-1], la capacité c_k >= poids des 力持ち de k+1 à j (en haut)
#
# On pré-calcule le poids cumulé pour optimiser les calculs.

N = int(sys.stdin.readline())
powers = []
weights = []
for _ in range(N):
    c, w = map(int, sys.stdin.readline().split())
    powers.append(c)
    weights.append(w)

# Pré-calcul des poids cumulés pour un accès en O(1)
# cum_weights[i] = somme des poids de 0 à i-1
cum_weights = [0] * (N + 1)
for i in range(N):
    cum_weights[i + 1] = cum_weights[i] + weights[i]

# Fonction qui retourne la somme des poids de l'intervalle [l, r] (inclus)
def sum_weight(l, r):
    return cum_weights[r + 1] - cum_weights[l]

# On crée un tableau pour marquer si les 力持ち de i à j peuvent être empilés dans cet ordre
can_stack = [[False] * N for _ in range(N)]

# Calcul de can_stack
# On vérifie pour chaque intervalle [i, j] si c'est possible d'empiler i en bas jusqu'à j en haut
for i in range(N):
    # une pile avec une seule personne est toujours possible
    can_stack[i][i] = True

for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        # On veut savoir si la pile i..j est possible
        # Condition : la pile i..j-1 est possible et le 力持ち en position j peut être placé au dessus,
        # et à chaque niveau, la capacité est suffisante pour supporter le poids au dessus.
        # Mais notre contrainte forte vient de vérifier que chaque 力持ち entre i et j-1 peut porter ceux au dessus.

        # On vérifie que la pile i..j-1 est valide
        if not can_stack[i][j - 1]:
            continue

        # On vérifie la capacité du 力持ち en position j-1 pour porter le dernier élément j
        # mais en fait ce contrôle est indirect car on vérifie la pile complète ci-dessous.

        # Vérifions toutes les capacités depuis i jusqu'à j-1
        possible = True
        for k in range(i, j):
            # Poids au dessus de k est poids (k+1..j)
            above_weight = sum_weight(k + 1, j)
            if powers[k] < above_weight:
                possible = False
                break
        if possible:
            can_stack[i][j] = True

# DP: dp[i] = nombre minimal de piles pour les 力持ち de 0 à i-1
dp = [10**9] * (N + 1)
dp[0] = 0  # 0 personnes => 0 piles

for i in range(1, N + 1):
    for j in range(i):
        if can_stack[j][i - 1]:
            # On peut créer une pile avec les 力持ち j..i-1,
            # donc on ajoute 1 pile aux piles nécessaires jusqu'à j-1
            if dp[j] + 1 < dp[i]:
                dp[i] = dp[j] + 1

print(dp[N])
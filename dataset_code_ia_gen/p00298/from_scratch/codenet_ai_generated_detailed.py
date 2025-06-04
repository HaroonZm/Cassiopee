import sys
sys.setrecursionlimit(10**7)

# On modélise chaque forceur comme un nœud qui peut soulever son voisin de gauche ou de droite selon les conditions.
# Le but est de former des piles en respectant les contraintes, et minimiser le nombre de piles (personnes au sol).

# Approche :
# - On modélise le problème comme un graphe où chaque forceur peut potentiellement soulever un ou plusieurs autres adjacents.
# - On cherche à "empiler" les forceurs au maximum, pour minimiser les racines des piles.
# - Utiliser une méthode de programmation dynamique basée sur la position dans la liste et les possibilités d'empilement d'un segment.
# - Ici, la condition empêche un forceur de soulever deux voisins simultanément, donc chaque pile est une chaîne simple.
# - On peut modéliser ça comme un problème de regroupement en sous-chaînes où chaque sous-chaîne est formée de forceurs empilés.
# - On va utiliser un DP où dp[i] = nombre minimal de piles pour couvrir les forceurs de i à N-1.
# - Pour chaque position i, on teste de faire une pile allant de i à j (j>=i), en vérifiant si l'empilement est valide.
# - La validation consiste à vérifier que chaque forceur peut soulever le suivant dans la pile.
# - Le poids total empilé doit respecter les capacités de levage.

# Implémentation détaillée ci-dessous :

N = int(sys.stdin.readline())
# capacities[i]: capacité max de levage du i-ème forceur
# weights[i]: poids du i-ème forceur
capacities = []
weights = []
for _ in range(N):
    c, w = map(int, sys.stdin.readline().split())
    capacities.append(c)
    weights.append(w)

# Pré-calcul des préfixes de poids pour obtenir rapidement le poids total d'un segment
prefix_weights = [0] * (N+1)
for i in range(N):
    prefix_weights[i+1] = prefix_weights[i] + weights[i]

# Fonction qui vérifie si l'on peut former une pile continue de forceurs de i à j (inclus)
# dans l'ordre i au sol, i+1 au-dessus, ..., j tout en haut.
def can_stack(i, j):
    # Pour valider qu'un empilement est possible, il faut que pour chaque forceur du bas
    # jusqu'à l'avant-dernier (du rang i à j-1), il puisse soulever la personne au-dessus.

    # En pile, le forceur i soulève i+1, i+1 soulève i+2, etc.
    # Le poids total à soulever par le forceur à la position k est le poids de tous les forceurs au-dessus (k+1 à j).
    # On doit vérifier: capacities[k] >= poids total de forceurs k+1 à j

    for k in range(i, j):
        # poids à soulever par k = somme poids indices (k+1) ... j
        total_weight = prefix_weights[j+1] - prefix_weights[k+1]
        if total_weight > capacities[k]:
            return False
    return True

# DP : dp[i] = nombre minimal de piles pour couvrir forceurs à partir de i
dp = [float('inf')] * (N+1)
dp[N] = 0  # aucun forceur à empiler après N-1

for i in range(N-1, -1, -1):
    # On essaie toutes les piles possibles qui commencent en i
    for j in range(i, N):
        if can_stack(i, j):
            # Si on peut empiler forceurs de i à j en une pile,
            # alors on ajoute 1 pile pour ce segment + dp[j+1]
            dp[i] = min(dp[i], 1 + dp[j+1])
        else:
            # Impossible d'empiler plus haut, arrêtons d'étendre la pile
            break

# dp[0] est la réponse : minimale des piles pour toute la rangée
print(dp[0])
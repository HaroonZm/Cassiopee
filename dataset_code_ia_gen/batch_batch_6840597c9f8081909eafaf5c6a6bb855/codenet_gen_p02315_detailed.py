# Solution complète pour le problème du sac à dos 0-1 en Python
# L'approche utilisée est la programmation dynamique (DP).

# Principe :
# On crée un tableau DP où dp[j] représente la valeur maximale
# que l'on peut obtenir avec une capacité j.
# Pour chaque item, on met à jour ce tableau en partant de la capacité maximale
# vers 0. On évite ainsi d'écraser les résultats intermédiaires
# pour les autres items.

# Complexité :
# Temps : O(N * W)
# Mémoire : O(W)

def knapsack_01():
    # Lecture des données
    N, W = map(int, input().split())
    items = []
    for _ in range(N):
        v, w = map(int, input().split())
        items.append((v, w))
    
    # Initialisation du tableau DP
    # dp[j] = valeur max avec une capacité j
    dp = [0] * (W + 1)
    
    # Parcours des items
    for value, weight in items:
        # On met à jour le dp en partant de la capacité max vers la capacité poids de l'objet
        for capacity in range(W, weight - 1, -1):
            # Choisir entre ne pas prendre ou prendre l'objet courant
            dp[capacity] = max(dp[capacity], dp[capacity - weight] + value)
    
    # Le résultat final est la valeur maximale pour la capacité W
    print(dp[W])

# Appel de la fonction principale
knapsack_01()
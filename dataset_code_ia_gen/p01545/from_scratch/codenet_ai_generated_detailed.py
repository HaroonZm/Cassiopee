# Problème résumé :
# On a une liste d'objets avec des poids distincts. Actuellement, ils sont dans un certain ordre.
# On veut les réarranger dans l'ordre croissant des poids.
# Pour déplacer un objet, on dépense une énergie égale à son poids.
# Le but est de minimiser la somme des poids des objets déplacés pour obtenir un ordre trié.

# Analyse :
# Le problème revient à transformer la permutation initiale en la permutation identité (ordre croissant).
# Chaque objet est identifié par son poids unique.
# La transformation minimale correspond à décomposer la permutation en cycles et
# minimiser le coût en traitant chaque cycle par la méthode suivante.

# Approche standard (cycle decomposition + formule de permutation minimale de somme de mouvements) :
# Soit un cycle C de taille k et poids des objets dans ce cycle : w_1, ..., w_k
# - Minimum du cycle : m_c = min(w_i)
# - Minimum global : m_g = min de tous les poids
# Coût de réorganisation du cycle :
# - Méthode 1 (interne au cycle) : déplacer tous mais un objet dans l’ordre avec un coût total
#   = somme des poids du cycle + (k-2)*m_c
# - Méthode 2 (utilisation du minimum global en dehors du cycle) :
#   = somme des poids du cycle + m_c + (k+1)*m_g
# On prend la méthode la moins chère pour ce cycle.

# On somme ça sur tous les cycles (de taille >= 2), les cycles de taille 1 ne demandent rien.

# Complexité : O(n) avec n jusqu'à 10^5, ce qui est efficace.

n = int(input())
weights = list(map(int, input().split()))

# Pour identifier la permutation, on récupère la position dans le tri
sorted_weights = sorted(weights)

# Créer un dictionnaire poids -> index dans le tri (permutation cible)
pos_in_sorted = {w: i for i, w in enumerate(sorted_weights)}

visited = [False] * n
total_cost = 0
global_min = min(weights)

for i in range(n):
    if visited[i]:
        continue
    # Décomposer le cycle
    cycle_indexes = []
    current = i
    cycle_sum = 0
    cycle_min = float('inf')
    cycle_len = 0
    
    # Suivre le cycle jusqu'à revenir au départ
    while not visited[current]:
        visited[current] = True
        w = weights[current]
        cycle_min = min(cycle_min, w)
        cycle_sum += w
        cycle_len += 1
        current = pos_in_sorted[w]  # position où devrait être cet objet
    
    # Si cycle_len > 1, calculer le coût
    if cycle_len > 1:
        # méthode 1 : interne au cycle
        cost1 = cycle_sum + (cycle_len - 2) * cycle_min
        # méthode 2 : utiliser le minimum global
        cost2 = cycle_sum + cycle_min + (cycle_len + 1) * global_min
        total_cost += min(cost1, cost2)
        
print(total_cost)
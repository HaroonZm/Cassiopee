n = int(input())
w = list(map(int, input().split()))

# On commence par définir certaines variables importantes :
# sorted_w : la liste w triée en ordre croissant
# index_map : dictionnaire pour trouver l'indice dans sorted_w d'une valeur donnée
sorted_w = sorted(w)
index_map = {val: idx for idx, val in enumerate(sorted_w)}
visited = [False] * n  # Pour marquer les éléments déjà traités

# On trouve le minimum global, il sera utile pour une stratégie alternative d'échange
global_min = sorted_w[0]

total_cost = 0

# L'idée générale est de décomposer la permutation initiale en cycles.
# Chaque cycle correspond à un ensemble d'éléments qui doivent être permutés entre eux pour être triés.
# Pour chaque cycle, on calcule le coût minimal pour le réarranger en ordre croissant.

for i in range(n):
    # Si déjà visité ou déjà à sa place, on passe
    if visited[i] or index_map[w[i]] == i:
        visited[i] = True
        continue

    cycle_sum = 0    # somme des valeurs dans le cycle
    cycle_min = float('inf')  # minimum dans le cycle
    cycle_len = 0    # taille du cycle
    j = i
    # On visite le cycle complet
    while not visited[j]:
        visited[j] = True
        val = w[j]
        cycle_min = min(cycle_min, val)
        cycle_sum += val
        j = index_map[val]
        cycle_len += 1

    # Deux méthodes pour réordonner le cycle:
    # 1) Faire les échanges à l'intérieur du cycle
    cost_method_1 = cycle_sum + (cycle_len - 2) * cycle_min
    # 2) Utiliser le minimum global comme "intermédiaire" pour réduire le coût
    cost_method_2 = cycle_sum + cycle_min + (cycle_len + 1) * global_min

    # On ajoute le coût minimal des deux méthodes
    total_cost += min(cost_method_1, cost_method_2)

print(total_cost)
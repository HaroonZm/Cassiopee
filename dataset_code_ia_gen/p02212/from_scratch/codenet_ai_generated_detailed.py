# Lecture des entrées : les ratings de 4 joueurs
a, b, c, d = map(int, input().split())

# On va tester toutes les manières de diviser les 4 joueurs en 2 équipes de 2 joueurs
# Chaque équipe est définie par une paire de joueurs, l'autre équipe est les deux restants
# Calculer la différence absolue des sommes des ratings des 2 équipes et chercher le minimum

# Liste des indices des joueurs
players = [a, b, c, d]

# Initiliser la différence minimale à une valeur très grande
min_diff = float('inf')

# Il existe 3 manières distinctes de séparer 4 joueurs en 2 équipes de 2
# On peut énumérer toutes les combinaisons possibles de 2 joueurs parmi 4
# Puis calculer la somme des 2 joueurs sélectionnés et la somme des autres joueurs
from itertools import combinations

for team1_indices in combinations(range(4), 2):
    # Indices de la première équipe
    team1_sum = players[team1_indices[0]] + players[team1_indices[1]]

    # Indices de la deuxième équipe : ceux qui ne sont pas dans team1_indices
    team2_indices = [i for i in range(4) if i not in team1_indices]
    team2_sum = players[team2_indices[0]] + players[team2_indices[1]]

    # Calculer la différence absolue
    diff = abs(team1_sum - team2_sum)

    # Mise à jour du minimum
    if diff < min_diff:
        min_diff = diff

# Afficher la différence minimale trouvée
print(min_diff)
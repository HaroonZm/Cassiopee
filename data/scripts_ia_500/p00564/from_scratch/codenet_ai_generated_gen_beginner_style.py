N,A,B,C,D = map(int, input().split())

# Calculer le nombre minimal de sets X nécessaires pour atteindre au moins N crayons
sets_x = (N + A - 1) // A
cost_x = sets_x * B

# Calculer le nombre minimal de sets Y nécessaires pour atteindre au moins N crayons
sets_y = (N + C - 1) // C
cost_y = sets_y * D

# Afficher le coût minimal entre les deux choix
print(min(cost_x, cost_y))
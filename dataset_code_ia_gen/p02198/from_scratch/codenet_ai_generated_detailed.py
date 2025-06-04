# Lecture des entrées depuis l'entrée standard
N, M = map(int, input().split())

# Calcul du nombre total de mandarines (ミカン)
# Chaque canette (アルミ缶) a M mandarines dessus,
# Il y a N canettes au total.
total_mikan = N * M

# Affichage du résultat suivi d'un saut de ligne
print(total_mikan)
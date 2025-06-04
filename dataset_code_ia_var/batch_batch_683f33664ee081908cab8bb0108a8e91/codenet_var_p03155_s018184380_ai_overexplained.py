# Demande à l'utilisateur de saisir une valeur entière pour N (premier entier)
N = int(input())  # input() récupère une chaîne de caractères ; int() convertit la chaîne en un entier

# Demande à l'utilisateur de saisir une valeur entière pour H (hauteur du rectangle)
H = int(input())  # input() récupère une chaîne de caractères ; int() convertit la chaîne en un entier

# Demande à l'utilisateur de saisir une valeur entière pour W (largeur du rectangle)
W = int(input())  # input() récupère une chaîne de caractères ; int() convertit la chaîne en un entier

# Calcule le nombre de façons de placer un rectangle de taille HxW dans un carré NxN
# (N-H+1) représente le nombre total de positions possibles verticalement (lignes)
# (N-W+1) représente le nombre total de positions possibles horizontalement (colonnes)
# On multiplie les deux pour avoir le nombre total de placements possibles
resultat = (N - H + 1) * (N - W + 1)  # Effectue la soustraction, puis la multiplication

# Affiche le résultat du calcul à l'utilisateur
print(resultat)  # print() affiche la valeur calculée à l'écran
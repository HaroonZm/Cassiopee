# Définition de la fonction M selon l'énoncé
def M(x, y):
    # Cas où le premier animal est Tanuki (T)
    if x == 'T':
        if y == 'T':
            return 'T'
        else:  # y == 'F'
            return 'F'
    else:  # x == 'F'
        if y == 'T':
            return 'T'
        else:  # y == 'F'
            return 'T'

# Lecture des données d'entrée
N = int(input())
P = input().split()

# On initialise le résultat avec le premier animal
result = P[0]

# On applique la fonction M de manière séquentielle sur les animaux donnés
for i in range(1, N):
    result = M(result, P[i])

# Affichage du résultat final suivi d'un saut de ligne
print(result)
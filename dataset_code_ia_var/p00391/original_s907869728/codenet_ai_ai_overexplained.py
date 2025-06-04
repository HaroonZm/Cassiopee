import sys  # Importation du module sys pour accéder à sys.exit()

# Lecture de deux entiers depuis l'entrée utilisateur sur une seule ligne, séparés par un espace.
# Exemple d'entrée : "3 4" assignera 3 à w et 4 à h
w, h = map(int, input().split())

# Initialisation de deux variables pour stocker la somme totale des colonnes (sumC) et des lignes (sumR)
sumC = 0
sumR = 0

# Lecture d'une liste de w entiers représentant les contraintes par colonne
# Exemple d'entrée : "2 1 2" pour w = 3, ce qui produira la liste [2, 1, 2]
col = list(map(int, input().split()))

# Lecture d'une liste de h entiers représentant les contraintes par ligne
# Exemple d'entrée : "3 1 1 0" pour h = 4, ce qui produira la liste [3, 1, 1, 0]
row = list(map(int, input().split()))

# Boucle sur chaque élément c de la liste col
# On incrémente sumC à chaque étape par la valeur de c (addition des contraintes colonnes)
for c in col:
    sumC += c

# Boucle sur chaque élément r de la liste row
# On incrémente sumR à chaque étape par la valeur de r (addition des contraintes lignes)
for r in row:
    sumR += r

# Vérification que la somme des contraintes par ligne (sumR) est égale à la somme des contraintes par colonne (sumC)
# Si elles ne sont pas égales, il est impossible de satisfaire à la fois les contraintes de lignes et de colonnes
if sumR != sumC:
    print(0)  # Affiche 0, signifiant que c'est impossible
    sys.exit(0)  # Interrompt immédiatement l'exécution du programme

# Boucle principale pour chaque colonne (allant de 0 inclus à w exclu)
for i in range(w):
    # Trie la liste 'row' en ordre décroissant avant chaque traitement de colonne
    # Ceci garantit que l'on commence par les lignes qui ont le plus de cases restantes à remplir
    row.sort(reverse=True)
    # Boucle imbriquée : parcours toutes les lignes pour la colonne en cours
    for j in range(h):
        # Vérifie si la contrainte de la colonne courante ou de la ligne courante est épuisée (0)
        # Si l'une des deux est égale à 0, on arrête la répartition pour cette colonne
        if not col[i] or not row[j]:
            break  # Sortie de la boucle sur j
        # Décrémente de 1 la contrainte ligne car on place un "casier" dans la cellule [j][i]
        row[j] -= 1
        # Décrémente de 1 la contrainte de la colonne courante car on y place aussi un "casier"
        col[i] -= 1
    # Après avoir parcouru toutes les lignes, vérifie s'il reste des contraintes non satisfaites pour la colonne i
    if col[i] > 0:
        print(0)  # On ne peut pas satisfaire la configuration, donc on affiche 0
        sys.exit(0)  # Interrompt le programme immédiatement car c'est impossible

# Si on atteint cette ligne, toutes les contraintes de lignes et de colonnes peuvent être satisfaites simultanément
print(1)  # Affiche 1 pour indiquer le succès (configuration possible)
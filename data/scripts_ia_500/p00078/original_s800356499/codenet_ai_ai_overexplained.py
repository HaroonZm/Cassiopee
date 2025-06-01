# Aizu Problem 0078: Magic Square
#
import sys, math, os  # Importation des modules système, mathématiques et d'OS pour interaction avec l'environnement

# Lecture de l'entrée standard si variable d'environnement PYDEV est configurée - permet de faciliter les tests locaux
PYDEV = os.environ.get('PYDEV')  # Récupération de la variable d'environnement 'PYDEV' pour savoir si on est en mode développement
if PYDEV == "True":  # Si la variable PYDEV est la chaîne "True"
    # On redirige l'entrée standard vers un fichier texte nommé "sample-input.txt" en mode lecture texte
    sys.stdin = open("sample-input.txt", "rt")

def magic_square(n):
    # Fonction qui construit un carré magique d'ordre n (n x n)
    # Un carré magique est un tableau n x n rempli de nombres distincts de 1 à n^2
    # où la somme des nombres dans chaque ligne, chaque colonne et les deux diagonales est la même.

    # Initialisation d'une matrice (liste de listes) 16x16 remplie de 0, même si on n'en utilise qu'une sous-partie n x n.
    # On utilise 16 par 16 pour garantir une zone suffisante pour manipuler les indices sans dépassement temporaire.
    sq = [[0 for _ in range(16)] for __ in range(16)]

    # Placement initial de 1 dans la position centrale légèrement décalée
    # nowx (coordonnée x actuelle) est à la moitié entière de n
    nowx = n // 2  
    # nowy (coordonnée y actuelle) est un cran au-dessous de nowx (indice y)
    nowy = n // 2 + 1  

    # Place le nombre 1 dans la cellule sq[nowy][nowx]
    # Dans une liste de listes en Python, sq[y][x] signifie rangée y, colonne x
    sq[nowy][nowx] = 1

    # Boucle pour placer tous les nombres suivants de 2 jusqu'à n^2 (car il y a n*n nombres à placer dans le carré)
    for i in range(2, n**2 + 1):
        # On déplace la position de 1 vers le coin inférieur droit (diagonale descendante vers la droite)
        nowx += 1  
        nowy += 1  

        # Boucle infinie pour trouver la bonne position pour le nombre i
        while True:
            # Si maintenant nowx dépasse la limite droite (>= n), on revient sur la première colonne (0)
            if nowx >= n:
                nowx = 0
            # Si maintenant nowx est devenu négatif, on va à la dernière colonne (n - 1)
            if nowx < 0:
                nowx = n - 1
            # Si maintenant nowy dépasse la limite basse (>= n), on revient sur la première ligne (0)
            if nowy >= n:
                nowy = 0
            # Teste si la position sq[nowy][nowx] est déjà occupée par un nombre non nul
            if sq[nowy][nowx] != 0:
                # Si case occupée, on recule vers la gauche (nowx - 1) et remonte la ligne (nowy + 1)
                nowx -= 1
                nowy += 1
            # On vérifie si la nouvelle position est libre et valide (dans le carré)
            # Le test s'assure que la case est à 0 (non encore utilisée)
            # et que les indices x et y sont bien compris entre 0 et n-1 inclus
            if sq[nowy][nowx] == 0 and 0 <= nowx < n and 0 <= nowy < n:
                # Si conditions remplies, on peut sortir de la boucle while et placer le numéro i
                break  
        # Placement du nombre i dans la case valide sq[nowy][nowx]
        sq[nowy][nowx] = i

    # Retourne la sous-matrice carrée n x n extraite de la matrice 16 x 16 (ne prend que les n premières lignes)
    return sq[:n]

# Boucle infinie principale pour traiter les cas de test
while True:
    # Lecture d'un entier n depuis l'entrée standard
    n = int(input())
    # Si n vaut 0, on sort de la boucle (condition d'arrêt)
    if n == 0:
        break
    # Sinon, on calcule le carré magique d'ordre n
    sq = magic_square(n)

    # Pour chaque rangée (ligne) du carré magique
    for row in sq:
        out = ""  # Initialisation de la chaîne de caractères qui contiendra la ligne formatée
        # Pour chaque nombre k dans la ligne, en ne prenant que les n premières colonnes
        for k in row[:n]:
            ks = str(k)  # Conversion du nombre en chaîne de caractères pour manipulation
            # Calcul du nombre d'espaces nécessaires pour que la chaîne fasse toujours 4 caractères de large
            ks = ' ' * (4 - len(ks)) + ks  # Ajoute des espaces avant le nombre pour alignement à droite
            out += ks  # Concatène le nombre formaté à la chaîne de sortie
        # Affiche la ligne formatée complète contenant les nombres alignés
        print(out)
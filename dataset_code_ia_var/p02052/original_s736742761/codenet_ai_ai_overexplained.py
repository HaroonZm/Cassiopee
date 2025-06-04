# Importation du module sys pour utiliser la fonction exit (commentée car non utilisée dans ce cas)
# from sys import exit

# Lecture d'une ligne d'entrée standard, contenant deux entiers séparés par un espace.
# 'input()' lit la ligne de texte, 'split()' la découpe en une liste de chaînes par les espaces.
# La compréhension de liste parcourt chaque chaîne 'n' dans la liste, et 'int(n)' la convertit en entier.
# La liste résultante contient donc deux entiers : 'H' pour la hauteur (nombres de lignes), 'W' pour la largeur (nombre de colonnes).
H, W = [int(n) for n in input().split()]

# Création initiale (remplie de zéros) d'une matrice ('c') de hauteur H et de largeur W.
# '[[0 for _ in range(W)] for __ in range(H)]' crée H listes imbriquées, chacune contenant W zéros.
# Cela sert à initialiser un tableau 2D où chaque case sera remplacée plus tard par les caractères de la saisie utilisateur.
c = [[0 for _ in range(W)] for __ in range(H)]

# Déclaration d'une liste vide appelée 'Bs'.
# Cette liste contiendra les coordonnées (indices de ligne et de colonne) de chaque cellule contenant un 'B'.
Bs = []

# Boucle sur toutes les lignes de la grille, de i=0 jusqu'à i=H-1.
for i in range(H):
    # Lecture d'une ligne d'entrée pour peupler la ligne i de la matrice.
    # 'input()' lit une chaîne de caractères ; 'str()' ici est redondant puisque 'input()' retourne déjà une chaîne.
    # 'list(...)' convertit la chaîne en une liste de caractères.
    c[i] = list(str(input()))
    
    # Boucle sur toutes les colonnes de la ligne en cours, de j=0 jusqu'à j=W-1.
    for j in range(W):
        # Si le caractère à la position (i, j) de la matrice est la lettre "B".
        if c[i][j] == "B":
            # Ajoute un tuple (i, j), représentant la position de 'B', à la liste 'Bs'.
            Bs.append((i, j))

# Initialisation d'une variable 'ans' à zéro.
# Celle-ci servira à stocker la plus grande distance trouvée entre deux positions de 'B'.
ans = 0

# Boucle imbriquée pour examiner chaque paire possible de 'B' dans la liste 'Bs'.
# 'e0' et 'e1' prendront chacune toutes les positions de 'B', y compris (éventuellement) la même position deux fois.
for e0 in Bs:
    for e1 in Bs:
        # Calcul de la distance de Manhattan entre les deux positions 'e0' et 'e1'.
        # La distance de Manhattan est la somme des valeurs absolues des différences de leurs coordonnées :
        # abs(e0[0] - e1[0]) est la différence verticale (ligne), abs(e0[1] - e1[1]) la différence horizontale (colonne).
        # 'max(ans, distance)' permet de mettre à jour 'ans' si la distance calculée est la plus grande rencontrée jusqu'ici.
        ans = max(ans, abs(e0[0] - e1[0]) + abs(e0[1] - e1[1]))

# Affichage de la valeur maximale trouvée pour la distance de Manhattan entre deux 'B'.
print(ans)
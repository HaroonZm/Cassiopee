def solve():
    # Lire une ligne de l'entrée standard, la diviser en une liste de chaînes, puis convertir chaque chaîne en entier grâce à map(int, ...)
    # Les résultats sont assignés respectivement à H (hauteur/grandeur du tableau), W (largeur du tableau)
    H, W = map(int, input().split())
    
    # Si la hauteur H vaut zéro, cela signifie généralement une condition d'arrêt (aucune matrice à traiter)
    if H == 0:
        # On retourne False pour indiquer qu'il n'y a plus rien à faire (utilisé pour sortir d'une boucle plus tard)
        return False

    # On va lire la grille ligne par ligne
    # MP initialisera une liste où chaque élément est une chaîne représentant une ligne dans le tableau
    # On utilise une compréhension de liste, qui évalue l'expression input() H fois (c'est une boucle for)
    # C'est équivalent à : 
    # MP = []
    # for i in range(H):
    #     MP.append(input())
    MP = [input() for i in range(H)]

    # Initialiser une matrice C de dimensions H x W remplie de zéros, ce sera une liste de listes
    # On fait une (nouvelle) liste de H éléments, chacun étant une liste de W zéros
    # Permet de stocker le nombre de cases vides ('.') consécutives vers le bas depuis chaque cellule (i, j)
    # [0]*W crée une liste de W zéros (par exemple [0, 0, 0, ...])
    # On met ça dans une boucle for sur range(H) pour obtenir H lignes
    C = [[0]*W for i in range(H)]

    # On va maintenant remplir la matrice C
    # Pour chaque colonne j (allant de 0 à W-1)
    for j in range(W):
        cnt = 0  # Compteur pour compter les cases vides consécutives vers le bas dans la colonne courante
        # On part de la dernière ligne (H-1), et on remonte jusqu'à la première ligne (indice 0), pas -1 pour s'arrêter
        for i in range(H-1, -1, -1):
            # Si la case correspond au caractère '.' (c'est-à-dire une case vide)
            if MP[i][j] == '.':
                cnt += 1  # On incrémente le compteur de cases vides consécutives
            else:
                cnt = 0   # Si la case n'est pas vide, on remet le compteur à zéro
            # On stocke la valeur courante du compteur dans la matrice C pour la cellule (i, j)
            # Cela indique à partir de (i, j), combien de cases vides consécutivement en dessous
            C[i][j] = cnt

    # Initialisation de la variable ans qui gardera la valeur maximale trouvée 
    # (dans ce contexte, la plus grande aire de sous-rectangle "vide" possible)
    ans = 0

    # Pour chaque ligne i (va de 0 à H-1)
    for i in range(H):
        # Initialiser une pile (stack) comme liste
        # On commence avec un élément (0, -1): (hauteur, position à gauche fictive)
        st = [(0, -1)]  

        # Pour chaque colonne j (de 0 à W-1)
        for j in range(W):
            # e prend la valeur pré-calculée C[i][j], c'est la hauteur du "rectangle" que l'on peut avoir à cet endroit
            e = C[i][j]

            # last gardera en mémoire la colonne de gauche pertinente pour ce contexte
            last = j

            # Tant que la pile n'est pas vide ET que la hauteur courante e est plus petite ou égale 
            # à la hauteur du sommet de la pile
            while st and e <= st[-1][0]:
                # On dépile le dernier élément, f = hauteur, k = indice colonne associée
                f, k = st.pop()
                # On calcule l'aire possible avec cette hauteur sur la largeur allant de k+1 à j
                # (j - k) * f : largeur * hauteur
                ans = max(ans, (j - k) * f)
                # On propage la position la plus à gauche pour l'élément suivant
                last = k

            # On ajoute l'élément (hauteur courante, dernière colonne connue)
            st.append((e, last))

        # À la fin de la ligne, il peut rester des éléments dans la pile
        # Il faut calculer les aires pour ceux-ci aussi (se prolongeant jusqu'à la fin de la ligne, c'est-à-dire W)
        while st:
            f, k = st.pop()
            # Pour chaque (f, k), calculer l'aire possible comme précédemment
            # (W - k) * f calcule la largeur depuis k+1 jusqu'à la fin (W-1)
            ans = max(ans, (W - k) * f)

    # Après avoir traité toutes les lignes, on affiche la réponse finale (l'aire maximale trouvée)
    print(ans)

    # On retourne True pour signaler que l'on peut continuer la boucle dans le code appelant
    return True

# Boucle principale
# On continue d'appeler solve() tant que celle-ci retourne True
# Lorsque solve() retourne False, cela arrête la boucle
while solve():
    # Les points de suspension indiquent simplement un bloc vide ici : aucune opération, on passe à l'itération suivante ou on quitte si False
    ...
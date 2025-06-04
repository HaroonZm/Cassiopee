# Lecture des dimensions de la grille : H (hauteur) et W (largeur)
# Utilise map pour convertir les entrées en entiers, input() pour lire une ligne, split() pour séparer sur les espaces
H, W = map(int, input().split())

# Initialisation de la variable de réponse "ans"
# On suppose que la plus grande zone possible, au départ, est la taille maximale entre H et W, c'est-à-dire la hauteur ou la largeur
ans = max(H, W)

# Lecture de la grille S : une liste de chaînes de caractères
# Pour chaque ligne (i) de 0 à H-1, on lit une entrée qui doit correspondre à une ligne de la grille
S = [input() for i in range(H)]

# Initialisation de T, une matrice qui gardera des infos sur les zones valides
# Ici, nous créons une première ligne de T contenant (W-1) zéros
T = [[0] * (W - 1)]

# Parcours de chaque zone de la grille (sauf la dernière ligne), pour construire T ligne par ligne
for i in range(H - 1):
    t = []      # Liste temporaire pour stocker les états de chaque sous-zone (1 si impair, 0 si pair)
    ts = []     # Nouvelle ligne qui sera ajoutée à T et contiendra les "hauteurs" de rectangles valides pour chaque colonne
    # Parcours de chaque colonne (sauf la dernière), pour regarder les sous-zones 2x2
    for j in range(W - 1):
        # On construit une chaîne 'r' qui représente les 4 caractères du carré 2x2 commençant en (i,j)
        # S[i][j:j+2] donne les deux caractères à la colonne j et j+1 de la ligne i
        # S[i+1][j:j+2] fait pareil pour la ligne suivante
        r = S[i][j:j+2] + S[i+1][j:j+2]
        # On compte le nombre de points (".") dans la zone r, puis on prend modulo 2 (pair/impair)
        t.append(r.count('.') % 2)
        # Si le nombre est pair (t[j]==0), cela signifie que le carré 2x2 satisfait la condition
        if t[j] == 0:
            # Dans ce cas, on ajoute 1 à la hauteur précédente de cette colonne (empilement)
            ts.append(T[-1][j] + 1)
        else:
            # Sinon, la condition n'est pas satisfaite, on remet à 0
            ts.append(0)
    # Une fois la ligne "ts" construite, on l'ajoute à T
    T.append(ts)

# On passe maintenant à l'analyse de T, pour déterminer la plus grande aire valide
# On ignore la première ligne de T (T[1:]), car elle sert d'initialisation
for L in T[1:]:
    # Utilisation d'une pile "stack" pour garder construit des rectangles, comme dans l'algorithme classique de la plus grande aire d'un histogramme
    stack = []
    # On parcourt chaque valeur l dans L, avec son indice i. On ajoute un 0 en fin de L pour vider la pile à la fin
    for i, l in enumerate(L + [0]):
        w = -1        # w servira à stocker l'indice du rectangle dont on sort si on dépile
        # On dépile tant que la pile n'est pas vide et que la hauteur l courante est inférieure ou égale à la hauteur stockée au sommet de la pile
        while stack and stack[-1][1] >= l:
            # On dépile : w est la position du rectangle, h sa hauteur
            w, h = stack.pop()
            # On met à jour la réponse : aire maximale possible
            # h+1 car la hauteur réelle est h+1 (décalage), i - w + 1 est la largeur
            ans = max(ans, (h + 1) * (i - w + 1))
        if w != -1:
            # Si on a dépilé, on ajoute le rectangle de largeur plus grande en gardant le nouveau l en hauteur
            stack.append((w, l))
            # On continue à la prochaine itération sans ajouter (i, l)
            continue
        # Sinon, on ajoute (i, l) à la pile
        stack.append((i, l))

# Affichage final de la plus grande aire trouvée
print(ans)
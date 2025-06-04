# Définition d'une fonction appelée inpl, qui va permettre de lire les entrées de l'utilisateur
# et de les convertir en une liste d'entiers.
# La fonction utilise input() pour lire une ligne entrée par l'utilisateur.
# input() renvoie une chaîne de caractères avec éventuellement plusieurs nombres séparés par des espaces.
# split() sépare cette chaîne en une liste de sous-chaînes (chaque sous-chaîne correspondant à un nombre).
# map(int, ...) transforme chaque sous-chaîne en entier en utilisant la fonction int().
# list(...) transforme le map (un itérable) en une liste.
def inpl():  
    return list(map(int, input().split()))

# Utilisation de la fonction inpl pour lire deux entiers depuis l'entrée standard :
# On suppose que l'utilisateur va entrer deux entiers séparés par un espace (par exemple "3 4").
# H est assigné à la première valeur entrée (représentant généralement la hauteur ou le nombre de lignes).
# W est assigné à la deuxième valeur entrée (représentant généralement la largeur ou le nombre de colonnes).
H, W = inpl()

# Initialisation de la variable ans à 0 pour stocker la réponse finale (le maximum recherché plus tard dans le code).
ans = 0

# Création d'une liste appelée C, qui va contenir les chaînes de caractères représentant chaque ligne de la grille.
# Utilisation d'une compréhension de liste.
# [input() for _ in range(H)] : input() est appelée H fois, une pour chaque ligne de la grille.
# Chaque input() récupère une ligne (par exemple, une chaîne de caractères de 'W' caractères).
C = [input() for _ in range(H)]

# Début d'une boucle for qui va s'exécuter deux fois (i prend les valeurs 0 et 1).
# Cette boucle sert à traiter d'abord la grille "telle quelle", puis à la transposer (échanger lignes et colonnes)
# afin d'appliquer le même traitement colonne par colonne.
for i in range(2):
    # Création d'une liste L de taille H, initialisée à 0 : L sera utilisée pour stocker la position du premier 'B' de chaque ligne.
    L = [0]*H
    # Création d'une liste R de taille H, initialisée à 0 : R sera utilisée pour stocker la position du dernier 'B' de chaque ligne.
    R = [0]*H
    # Création d'une liste Lk vide : Lk va contenir les indices des lignes qui ont au moins un 'B'.
    Lk = []
    # Création d'une liste Rk vide : Rk va contenir également les indices des lignes qui ont au moins un 'B'.
    Rk = []
    # Boucle sur chaque ligne h de la grille (h varie de 0 à H-1).
    for h in range(H):
        # find("B") cherche la première occurrence du caractère 'B' dans la ligne C[h].
        # Si 'B' est trouvé, find renvoie son indice (de 0 à W-1), sinon il renvoie -1.
        # On stocke ce résultat dans L[h] (position du 1er 'B' dans la ligne h, -1 si absent).
        L[h] = C[h].find("B")
        # rfind("B") fait la même chose mais cherche la dernière occurrence de 'B'.
        # On stocke ce résultat dans R[h] (position du dernier 'B' dans la ligne h, -1 si absent).
        R[h] = C[h].rfind("B")
        # Si on a trouvé au moins un 'B' dans la ligne h (donc L[h] >= 0), on ajoute l'indice h à la liste Lk.
        if L[h] >= 0:
            Lk.append(h)
        # Si on a trouvé au moins un 'B' dans la ligne h (donc R[h] >= 0), on ajoute l'indice h à la liste Rk.
        if R[h] >= 0:
            Rk.append(h)

    # Boucle imbriquée pour calculer une valeur pour chaque paire (lh, rh), où lh est une ligne ayant un 'B' au moins,
    # et rh aussi.
    for lh in Lk:  # lh va être un indice de ligne où il y a au moins un 'B'
        for rh in Rk:  # rh aussi
            # Calcul de la valeur maximisée : on veut la distance horizontale absolue entre le premier 'B' de la ligne lh (L[lh])
            # et le dernier 'B' de la ligne rh (R[rh]), plus la distance verticale absolue entre lh et rh.
            # abs(L[lh] - R[rh]) calcule la distance horizontale entre ces positions.
            # abs(lh - rh) calcule la distance verticale entre ces lignes.
            # La somme donne une sorte de chemin ou distance potentielle entre deux 'B'.
            # On met à jour ans en prenant le maximum entre sa valeur actuelle et la nouvelle valeur calculée pour chaque paire.
            ans = max(ans, abs(L[lh] - R[rh]) + abs(lh - rh))

    # Si on est au premier tour de la boucle principale (i == 0), on transpose la grille C pour traiter les colonnes
    # comme des lignes au deuxième passage.
    if i == 0:
        # zip(*C) "déplie" (unpacks) la liste C afin de grouper les éléments de même position (colonne) dans chaque chaîne.
        # Chaque tuple retourné par zip(*C) correspond à une colonne de la grille initiale.
        # "".join(c) les transforme en chaînes de caractères, pour obtenir la grille transposée.
        C = ["".join(c) for c in zip(*C)]
        # On échange H et W car après la transposition, le nombre de lignes devient le nombre de colonnes et vice versa.
        H, W = W, H

# Enfin, on affiche la valeur finale de ans, qui représente le maximum trouvé selon le calcul décrit précédemment.
print(ans)
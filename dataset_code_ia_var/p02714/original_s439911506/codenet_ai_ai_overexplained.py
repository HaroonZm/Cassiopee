# Demande à l'utilisateur d'entrer un nombre entier, puis le convertit et le stocke dans la variable N.
# Cette variable représente le nombre de caractères qui seront traités par le programme.
N = int(input())

# Demande à l'utilisateur d'entrer une chaîne de caractères, puis la convertit en une liste de caractères.
# Chaque élément de la liste S correspond à un caractère individuel de la chaîne entrée.
S = list(input())

# Initialise trois listes vides :
# R stockera les indices des caractères 'R' (probablement pour "Red").
# G stockera les indices des caractères 'G' (probablement pour "Green").
# B stockera les indices des caractères 'B' (probablement pour "Blue").
R = []
G = []
B = []

# Initialise un compteur à zéro. Cette variable servira à compter le résultat final.
cnt = 0

# Parcourt chaque indice i de 0 jusqu'à N-1 pour examiner chaque caractère de la liste S.
for i in range(N):
    # Vérifie si le caractère à l'indice i de S est 'R'.
    if S[i] == "R":
        # Si oui, ajoute l'indice i à la liste R.
        R.append(i)
    # Si ce n'est pas un 'R', vérifie si c'est un 'G'.
    elif S[i] == "G":
        # Si oui, ajoute l'indice i à la liste G.
        G.append(i)
    # Si le caractère n'est ni 'R' ni 'G', il considère que c'est 'B' (car il n'y a que trois couleurs possibles).
    else:
        # Ajoute l'indice i à la liste B.
        B.append(i)

# Convertit la liste B en un ensemble pour accélérer la recherche d'éléments.
# Les ensembles permettent des recherches plus rapides que les listes via l'opérateur 'in'.
B = set(B)

# Calcule le nombre total d'indices de type 'B' en utilisant la fonction len() sur l'ensemble B,
# puis stocke cette valeur dans la variable b.
b = len(B)

# Boucle externe : Parcourt chaque indice i stocké dans la liste R (i.e., positions des 'R').
for i in R:
    # Boucle interne imbriquée : Parcourt chaque indice j stocké dans la liste G (i.e., positions des 'G').
    for j in G:
        # Initialise une variable check à 0 pour ce couple (i, j).
        # Cette variable servira à compter combien de cas particuliers sont détectés et seront soustraits plus tard.
        check = 0

        # Calcule le minimum (m) et maximum (M) des indices i et j.
        # Cela permet de simplifier le calcul des autres indices pertinents.
        m = min(i, j)
        M = max(i, j)

        # Calcule la distance r entre les indices M et m.
        r = M - m

        # Calcule l'indice situé à gauche (left) et à droite (right) à une distance r de m et M.
        left = m - r
        right = M + r

        # Vérifie si la distance r est paire (i.e., r % 2 == 0).
        # Cela permet de savoir s'il existe un centre exactement entre m et M.
        if r % 2 == 0:
            # Si c'est le cas, calcule l'indice du centre.
            center = m + r // 2
            # Vérifie si l'indice center fait partie de l'ensemble B.
            # Si oui, cela signifie qu'il y a un 'B' exactement entre le 'R' et le 'G'.
            if center in B:
                # Incrémente la variable check de 1 pour ce cas particulier.
                check += 1

        # Vérifie si l'indice left (donc symétrique à m par rapport à M) fait partie de l'ensemble B.
        if left in B:
            # Si oui, incrémente check de 1.
            check += 1

        # Vérifie si l'indice right (symétrique à M par rapport à m) appartient à l'ensemble B.
        if right in B:
            # Si oui, incrémente check de 1.
            check += 1

        # Calcule la différence entre le nombre total de 'B' (b) et le nombre de cas particuliers détectés (check).
        # Ajoute cette valeur à la variable de comptage totale (cnt).
        # Cela correspond au nombre de triplets où le 'B' choisi n'est PAS dans une des positions interdites.
        cnt += b - check

# Affiche la valeur totale finale du compteur cnt,
# qui représente le nombre total de façons de choisir un indice 'R', un indice 'G' et un indice 'B'
# ne formant pas un triplet interdit selon les conditions du problème.
print(cnt)
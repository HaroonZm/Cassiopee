def get_input():
    # Définition d'une fonction génératrice nommée get_input
    # qui lira des lignes de l'entrée standard jusqu'à EOF (fin de fichier).
    # Les générateurs permettent de produire une séquence de valeurs paresseusement
    # sans stocker toute la séquence en mémoire.
    while True:
        try:
            # On utilise input() pour lire une ligne de l'entrée standard.
            # input() retourne une chaîne de caractères sans le caractère de saut de ligne final.
            # la fonction join('') ici ne transforme pas la chaîne en liste mais concatène les éléments de
            # l'itérable donné (la chaîne de caractères est un itérable de caractères).
            # En fait ici, ''.join(input()) est redondant car input() est déjà une chaîne.
            # On yield cette chaîne pour la retourner au caller sans arrêter la fonction.
            yield ''.join(input())
        except EOFError:
            # Lorsqu'on atteint la fin de l'entrée standard,
            # une exception EOFError est levée. On l'attrape ici pour sortir
            # proprement de la boucle infinie et donc arrêter la génération.
            break

def nuri(table, m, x, y):
    # Définition d'une fonction récursive nommée nuri
    # qui effectue une sorte de propagation ou marquage sur une grille (table)
    # en utilisant une matrice m pour stocker les valeurs associées.
    # Les arguments table et m sont des listes de listes (matrices),
    # x et y sont des indices de position dans ces matrices.

    # Pour chaque direction (haut, bas, gauche, droite), on vérifie si
    # dans table la case est True et dans m la case est à 0,
    # pour décider de propager la valeur m[x][y].
    if table[x-1][y] and m[x-1][y] == 0:
        # Si la case au-dessus est True dans table et non marquée dans m
        # on copie la valeur de m[x][y] dans m[x-1][y]
        m[x-1][y] = m[x][y]
        # et on rappelle récursivement nuri pour continuer la propagation à cette nouvelle position
        nuri(table, m, x-1, y)
    if table[x+1][y] and m[x+1][y] == 0:
        # Même opération pour la case en dessous
        m[x+1][y] = m[x][y]
        nuri(table, m, x+1, y)
    if table[x][y-1] and m[x][y-1] == 0:
        # Même opération pour la case à gauche
        m[x][y-1] = m[x][y]
        nuri(table, m, x, y-1)
    if table[x][y+1] and m[x][y+1] == 0:
        # Même opération pour la case à droite
        m[x][y+1] = m[x][y]
        nuri(table, m, x, y+1)
    # La fonction ne retourne rien explicitement; elle modifie m en place.
    return

# Appel de la fonction get_input pour obtenir un générateur
# puis création d'une liste N contenant toutes les lignes lues de l'entrée
N = list(get_input())

# Traitement par blocs de 13 lignes (probablement une spécification spécifique au problème)
for l in range(0, len(N), 13):
    # Création d'une matrice 14x14 initialisée à False
    # pour stocker un tableau de booléens nommé table.
    # On utilise 14 pour créer une bordure afin d'éviter les erreurs d'index lors de la navigation.
    table = [[False for i in range(14)] for j in range(14)]

    # Boucle pour remplir la partie centrale (12x12) de la matrice table
    for i in range(12):
        for j in range(12):
            # Conversion du caractère en entier.
            # Si ce chiffre vaut 1, on affecte True dans la case correspondante de table,
            # décalée de 1 vers la droite et le bas pour respecter la bordure.
            if int(N[l+i][j]) == 1:
                table[i+1][j+1] = True

    # On crée une autre matrice 14x14 nommée m avec des entiers initialisés à zéro.
    # Cette matrice sert à marquer les régions connectées détectées dans table.
    m = [[0 for i in range(14)] for j in range(14)]

    # Initialisation d'un compteur pour compter le nombre de régions distinctes
    cnt = 0
    # Parcours des indices effectifs de la zone utile de table et m (de 1 à 12 inclus)
    for i in range(1, 13):
        for j in range(1, 13):
            # Si la case est True dans table et non marquée dans m (donc découverte)
            if table[i][j] and m[i][j] == 0:
                # Incrément du compteur de régions
                cnt += 1
                # Marquage initial de la case dans m avec le numéro de la région
                m[i][j] = cnt
                # Appel récursif à nuri pour propager ce numéro dans toute la région connectée
                nuri(table, m, i, j)

    # Affichage du nombre total de régions distinctes détectées dans ce bloc
    print(cnt)
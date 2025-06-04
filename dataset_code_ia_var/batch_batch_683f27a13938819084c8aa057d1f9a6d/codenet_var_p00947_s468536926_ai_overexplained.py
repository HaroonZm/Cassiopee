import copy  # On importe le module copy pour effectuer des copies profondes de listes

# Initialisation de la matrice T.
# T sera une liste de 10 listes, chacune contenant 10 entiers, soit une matrice 10x10.
# Pour cela, on lit 10 lignes depuis l'entrée standard (input).
# Chaque ligne est découpée en mots (séparés par des espaces), chaque mot est transformé en entier, et ces entiers forment une sous-liste.
# La compréhension de liste s'exécute 10 fois, une fois pour chaque ligne d'entrée.
T = [[int(x) for x in input().split()] for i in range(10)]

def E(ID):
    '''
    La fonction E prend en argument une liste de 4 éléments (ID) représentant des chiffres sous forme de chaînes de caractères.
    Son but est de parcourir la matrice T via les chiffres de l'identifiant pour en obtenir un résultat selon une suite d’états.
    '''
    ret = 0  # On initialise la variable ret à 0, c'est la position actuelle dans T.
    for d in ID:  # On parcourt chaque chiffre (sous forme de chaîne) dans ID.
        d = int(d)  # On convertit la chaîne de caractère en entier
        ret = T[ret][d]  # On se déplace selon la valeur d dans la matrice T, ligne ret, colonne d.
    return ret  # La fonction retourne la valeur finale de ret après 4 transitions.

def solve(ID):
    '''
    La fonction solve détermine si, pour un identifiant donné (ID, liste de 4 chiffres sous forme de chaînes),
    certaines opérations de modification rendent une condition vérifiée sur la matrice T.
    La fonction retourne 1 si la condition est remplie au moins une fois pour certaines modifications, sinon 0.
    '''
    e = E(ID)  # On calcule l'état e obtenu en appliquant la fonction E à l'identifiant ID.

    # Première boucle : on tente de modifier chaque chiffre de ID (4 chiffres),
    # en essayant de remplacer chacun d'eux par tous les chiffres possibles de 0 à 9 (sauf si la valeur est identique).
    for i in range(4):  # On parcourt l'indice de chaque position dans ID (0 à 3).
        for j in range(10):  # On teste chaque chiffre possible de 0 à 9 pour la position i.
            kari = copy.deepcopy(ID)  # On fait une copie profonde de ID dans kari pour pouvoir modifier sans altérer l'original.
            if kari[i] == str(j):  # Si le chiffre à la position i est déjà égal à j, on ne change rien et on continue.
                continue
            kari[i] = str(j)  # On remplace le chiffre à la position i par j (sous forme de chaîne).
            # On vérifie si la valeur à la position [E(kari)][e] dans T est égale à 0.
            # E(kari) donne un état de départ après la modification, e est l'état original.
            if T[E(kari)][e] == 0:
                return 1  # Si c'est le cas, on retourne 1 immédiatement (condition satisfaite).

    # Deuxième boucle : On regarde si dans la ligne correspondant à E(ID), il existe un chemin ouvert (valeur 0) vers n'importe quel état (i),
    # à l'exception de e lui-même.
    for i in range(10):  # Parcours des indices de colonnes (0 à 9) de la matrice T pour la ligne E(ID).
        if T[E(ID)][i] == 0 and i != e:  # Si la valeur est 0 et la colonne i est différente de e
            return 1  # On retourne 1 (condition satisfaite).

    # Troisième boucle : on échange deux chiffres consécutifs dans ID et on vérifie si cela satisfait la condition [E(kari)][e]==0
    for i in range(3):  # On va de 0 à 2 pour échanger chaque paire consécutive (0-1, 1-2, 2-3)
        kari = copy.deepcopy(ID)  # Nouvelle copie profonde de ID modifiable.
        if kari[i] == kari[i+1]:  # Si les deux chiffres consécutifs sont identiques, l'échange ne change rien, donc on saute.
            continue
        # On échange les valeurs à la position i et i+1
        kari[i], kari[i+1] = kari[i+1], kari[i]
        if T[E(kari)][e] == 0:  # Si la valeur à [E(kari)][e] dans T est 0, la condition est satisfaite.
            return 1

    # Dernière vérification : on construit un nouvel identifiant composé des 3 premiers chiffres de ID et du chiffre e obtenu précédemment.
    # On vérifie si la transition de ce nouvel identifiant vers la dernière valeur de ID est ouverte (valeur de T à 0)
    # et que ce dernier chiffre est différent de e.
    # ID[:3] prend les trois premiers chiffres, [str(e)] ajoute e sous forme de chaîne,
    # et on vérifie T[ E( ID[:3]+[str(e)] ) ][ int(ID[3]) ] == 0
    if T[E(ID[:3] + [str(e)])][int(ID[3])] == 0 and int(ID[3]) != e:
        return 1

    # Si aucune des conditions n’a été satisfaite, on retourne 0 pour cet identifiant.
    return 0

ans = 0  # Initialisation du compteur de réponse à 0.

# On parcourt tous les entiers de 0 à 9999 inclus (total de 10000 identifiants possibles à 4 chiffres).
for i in range(10000):
    ID = [j for j in str(i)]  # On découpe l'entier i en une liste de caractères (représente les chiffres).
    ID = ['0'] * (4 - len(ID)) + ID  # On ajoute des zéros initiaux pour s’assurer que ID fasse toujours 4 caractères.
    ans += solve(ID)  # On appelle la fonction solve(ID) et on ajoute son résultat à ans.

print(ans)  # On affiche la valeur finale de ans.
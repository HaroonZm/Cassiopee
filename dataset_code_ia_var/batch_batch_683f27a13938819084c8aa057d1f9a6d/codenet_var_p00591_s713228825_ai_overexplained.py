import sys  # Le module sys permet d’accéder à certaines variables utilisées ou maintenues par l’interpréteur, ici pour lire les entrées standard.

def get_min_value_in_row(data):
    # Cette fonction prend en argument une liste "data" représentant une ligne d'une matrice.
    # Elle retourne l'index de la plus petite valeur dans cette ligne.
    if len(data) < 1:
        # Si la longueur de la ligne est nulle (la ligne est vide), alors on retourne 0.
        return 0
    min = 0  # On initialise l'index du minimum à 0.
    for i in range(0, len(data)):
        # On commence une boucle allant de 0 à la longueur de la liste data.
        # Pour chaque élément de data à l'index i :
        if data[i] < data[min]:
            # Si l'élément en position i est inférieur à celui actuellement stocké comme minimum,
            # alors on met à jour min avec l'index i.
            min = i
    # Après la boucle, min contient l'index de la valeur minimale dans la ligne.
    return min

def is_max(Min, index, data):
    # Cette fonction vérifie si l'élément situé à la ligne d'indice "index" et à la colonne d'indice "Min"
    # est le maximum dans sa colonne dans toute la matrice "data".
    # Min : l’index de la colonne à vérifier.
    # index : l’index de la ligne où se trouve la valeur potentiellement max.
    # data : la matrice, c'est-à-dire une liste de listes d'entiers.
    max = data[index][Min]  # On initialise la variable max à la valeur cible.
    for i in range(index, -1, -1):
        # Première boucle allant de l’index courant jusque la première ligne (inclus), en décrémentant i.
        # Cela permet de vérifier toutes les valeurs dans la colonne Min du haut jusqu'à la ligne actuelle.
        if data[i][Min] > max:
            # Si une valeur lue dans la colonne Min (pour la ligne i) est supérieure à max,
            # alors on met max à jour avec cette nouvelle valeur.
            max = data[i][Min]
    for i in range(index, len(data)):
        # Deuxième boucle allant de la ligne actuelle jusqu'à la dernière ligne incluse.
        # Permet de vérifier le reste des lignes dans la colonne.
        if data[i][Min] > max:
            # Même logique que précédemment : mise à jour de max si une valeur plus grande est trouvée.
            max = data[i][Min]
    # Enfin, on retourne True si la valeur du départ (data[index][Min]) est effectivement le maximum trouvé dans cette colonne.
    # Sinon, on retourne False.
    return True if max == data[index][Min] else False

def print_both(data):
    # Cette fonction affiche la valeur qui est le minimum de sa ligne ET le maximum de sa colonne, s'il y en a une.
    # Si aucune valeur ne correspond à ces critères, affiche 0.
    for i in range(0, len(data)):
        # On parcourt chaque ligne de la matrice.
        indexmin = get_min_value_in_row(data[i])
        # On trouve l'index de la valeur minimale dans la ligne i.
        if is_max(indexmin, i, data) == True:
            # On vérifie que ce minimum est aussi le maximum de sa colonne.
            print(data[i][indexmin])  # Si oui, on affiche la valeur.
            return  # On arrête la fonction dès qu’un tel élément est trouvé.
    # Si la boucle se termine sans avoir trouvé de valeur répondant au critère, on affiche 0.
    print(0)

# Initialisation d’une liste vide qui va contenir toutes les lignes lues en entrée standard.
l = []
for i in sys.stdin:
    # On ajoute chaque ligne lue depuis l'entrée standard à la liste l.
    l.append(i)

i = 0  # On initialise l'index i à zéro, il sert à parcourir la liste l.
while i < len(l):
    # Tant que i est inférieur à la longueur de la liste l (donc on n’a pas tout parcouru) :
    if len(l[i]) == 2:
        # Ici, on suppose qu’une ligne qui contient exactement 2 caractères est un nombre
        # (typiquement, c'est le num. de lignes de la matrice, attendu en entrée).
        Matrix = []  # La matrice sera stockée dans cette liste.
        for j in range(i+1, int(l[i]) + i + 1):
            # On lit les lignes suivantes, qui contiennent les données de la matrice,
            # Le nombre de lignes à lire est donné par int(l[i])
            temp = [l[j].split()]  # On découpe la ligne en liste de chaînes représentant les entiers.
            for k in range(0, len(temp[0])):
                # Pour chaque élément dans la liste temp[0], on le convertit en entier.
                temp[0][k] = int(temp[0][k])
            Matrix.append(temp[0])  # On ajoute la ligne convertie à la matrice.
        i += int(l[i]) + 1  # On saute à l’index de la prochaine matrice dans l’entrée.
        print_both(Matrix)  # On appelle la fonction de traitement et d’affichage pour la matrice lue.
    else:
        # Si la ligne actuelle n’est pas une ligne d’entête (i.e. de taille 2), on passe à la suivante.
        i += 1
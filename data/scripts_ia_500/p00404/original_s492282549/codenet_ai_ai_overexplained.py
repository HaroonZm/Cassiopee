import sys  # Importation du module sys pour utiliser sys.exit() qui permet de terminer le programme prématurément

# Lecture d'une ligne de l'entrée standard, découpage en éléments séparés par des espaces, conversion de chacun en entier,
# puis création d'une liste appelée 'point' contenant ces entiers.
point = list(map(int, input().split()))

# Vérification si le premier élément de 'point' (point[0]) est égal à 0 ET le second élément (point[1]) est égal à 0.
# Cela signifie que le point est à l'origine (0,0) sur un plan cartésien.
if point[0] == 0 and point[1] == 0:
    # Si la condition précédente est vraie, alors on affiche "1"
    print("1")
    # Puis on termine immédiatement le programme, il n'y a plus rien à exécuter après ceci.
    sys.exit()

# Initialisation d'une liste appelée 'fiblist' contenant les trois premiers nombres utilisés pour la suite
# initialement 0, 1, et 1, ce qui est proche des premiers termes d'une suite de Fibonacci étendue.
fiblist = [0, 1, 1]

# Création d'une liste 'maxpoint' avec deux éléments initialisés à 0, représentant les valeurs maximales initiales pour les abscisses (x) et ordonnées (y).
maxpoint = [0, 0]

# Création d'une liste 'minpoint' avec deux éléments initialisés à 0, représentant les valeurs minimales initiales pour les abscisses (x) et ordonnées (y).
minpoint = [0, 0]

# Initialisation d'un compteur entier 'i' à 2, qui sera utilisé pour suivre l'itération dans la boucle.
i = 2

# Boucle infinie; elle continuera de tourner jusqu'à ce qu'on appelle 'break' pour sortir explicitement.
while True:
    # Calcul du reste de la division de i par 4. Si ce reste est 2 ou 3 :
    if i % 4 == 2 or i % 4 == 3:
        # On ajoute à la valeur de 'maxpoint' à l'indice i % 2 (donc 0 ou 1)
        # la valeur fiblist[2], le dernier élément calculé de la liste fiblist.
        # Cette condition permet de mettre à jour la borne maximale pour la coordonnée x ou y selon la parité de i.
        maxpoint[i % 2] += fiblist[2]
    else:
        # Sinon, si i % 4 est 0 ou 1, on soustrait fiblist[2] à minpoint à l'indice i % 2.
        # Cela met à jour la borne minimale pour la coordonnée x ou y selon la parité de i.
        minpoint[i % 2] -= fiblist[2]

    # Vérification complexe pour voir si le point donné en entrée est contenu dans le rectangle défini par
    # les bornes minimales et maximales sur les x et y.
    # point[0] est la coordonnée x, point[1] la coordonnée y.
    if minpoint[0] <= point[0] and maxpoint[0] >= point[0] and minpoint[1] <= point[1] and maxpoint[1] >= point[1]:
        # Si le point est dans ce rectangle défini par (min_x, max_x) et (min_y, max_y),
        # on calcule (i-1) modulo 3, on ajoute 1, puis on affiche ce résultat.
        # Cela est probablement un indicateur ou un index cyclique en fonction de l'itération.
        print((i - 1) % 3 + 1)
        # On casse la boucle infinie pour arrêter l'exécution en sortant de la boucle.
        break

    # Mise à jour des éléments dans 'fiblist' pour passer au nombre de Fibonacci suivant.
    # On décale fiblist[1] vers fiblist[0] et fiblist[2] vers fiblist[1].
    fiblist[0] = fiblist[1]
    fiblist[1] = fiblist[2]
    # Le nouveau fiblist[2] devient la somme des deux nombres précédents, conformément à la définition de Fibonacci.
    fiblist[2] = fiblist[0] + fiblist[1]

    # Incrémentation de i de 1 pour passer à la prochaine itération.
    i += 1
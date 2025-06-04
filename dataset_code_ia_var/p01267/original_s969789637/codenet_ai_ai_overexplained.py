# Démarre une boucle infinie, c'est-à-dire une boucle qui ne s'arrêtera jamais d'elle-même,
# sauf si une condition de sortie avec 'break' est atteinte à l'intérieur de la boucle.
while True:
    # Lit une ligne depuis l'entrée standard (généralement le clavier),
    # sépare la ligne en sous-chaînes selon les espaces,
    # puis convertit chaque sous-chaîne en un entier grâce à map(int, ...),
    # et affecte ces cinq valeurs à n, a, b, c, x respectivement.
    n, a, b, c, x = map(int, input().split())
    
    # Vérifie si la variable n est égale à 0, ce qui représente un cas de terminaison.
    # Si c'est vrai, on sort de la boucle en utilisant 'break'.
    if n == 0:
        break

    # Initialise une variable 'flame' à 0.
    # Cette variable sert de compteur pour indiquer le nombre d'itérations ou "tentatives".
    flame = 0
    
    # Initialise un booléen 'first' à True.
    # Il permet de savoir si on traite le tout premier élément dans le bloc for ci-après.
    first = True

    # Lit une nouvelle ligne de l'entrée utilisateur,
    # la découpe selon les espaces, convertit chaque sous-chaîne en entier,
    # puis la convertit en une liste de ces entiers.
    # On parcourt cette liste grâce à une boucle for, chaque valeur étant stockée dans 'y'.
    for y in list(map(int, input().split())):
        # Si ce n'est pas le tout premier élément de la liste (first == False):
        if not first:
            # On met à jour la variable x en appliquant la transformation linéaire :
            # x = (a * x + b) % c
            # Cette opération modifie x à chaque itération sauf la toute première.
            x = (a * x + b) % c
            # On incrémente le compteur 'flame' de 1 pour chaque opération ci-dessus.
            flame += 1
        else:
            # Si on traite le premier élément seulement, on passe first à False
            # pour éviter de répéter ce bloc la fois suivante.
            first = False

        # On entre dans une boucle while dont le but est de faire évoluer x
        # jusqu'à ce qu'il soit égal à la valeur cible y, ou qu'on dépasse 10000 étapes.
        while x != y and flame <= 10000:
            # Met à jour x selon la fonction de transformation.
            x = (a * x + b) % c
            # Incrémente le nombre de tentatives/recherches/flammes.
            flame += 1

    # Après la boucle, on vérifie si le compteur 'flame' a dépassé la limite de 10000.
    # Si c'est le cas, cela signifie que la séquence n'a pas pu être réalisée dans le nombre de tentatives imposé,
    # donc on imprime -1 pour signaler l'échec.
    if flame > 10000:
        print(-1)
    else:
        # Sinon, on affiche simplement le nombre d'étapes effectuées.
        print(flame)
# Début d'une boucle infinie "while", qui ne peut s'arrêter que par un 'break'.
while True:
    # Lecture d'une ligne d'entrée utilisateur contenant 3 entiers. 'raw_input()' lit une ligne de texte, puis on la découpe à l'aide de 'split()'.
    # 'map(int, ...)' applique la conversion en entier à chacun des éléments obtenus après division de la chaine.
    i, j, k = map(int, raw_input().split())

    # Vérification d'arrêt : si les trois entiers lus sont égaux à 0 simultanément, on interrompt la boucle infinie grâce à 'break'.
    if i == 0 and j == 0 and k == 0:
        break

    # Calcul de la somme totale des trois entrées. Servira probablement à fixer une taille ou le nombre total d'éléments à traiter.
    n = i + j + k

    # Initialisation d'une liste vide nommée 's'.
    # Elle servira à stocker des ensembles selon une certaine condition plus loin dans le code.
    s = []

    # Création d'un ensemble 'a' constitué de tous les entiers de 0 à n-1 (c'est le résultat de 'range(n)')
    # Cela représente probablement l'ensemble complet des indices possible.
    a = set(range(n))

    # Initialisation de deux ensembles vides nommés 'b' et 'c'.
    # Ils serviront à mémoriser/inclure des indices particuliers selon certaines logiques ultérieures.
    b = set()
    c = set()

    # Boucle sur un certain nombre d'itérations, déterminé par la valeur saisie par l'utilisateur via 'input()'.
    # Attention : 'input()' (en Python 2) lit et évalue une expression. On suppose ici que ce code est Python 2.
    for i in range(input()):
        # Lecture de quatre entiers en une seule ligne. Voir commentaire plus haut sur la lecture/partition/conversion.
        x, y, z, r = map(int, raw_input().split())

        # Décrémentation de chacun des indices de 1, car visiblement l'entrée est en base 1 (humain), alors que le code utilise la base 0.
        x -= 1
        y -= 1
        z -= 1

        # Si r est égal à zéro : on construit un ensemble avec x, y, z et on l'ajoute à la liste 's'.
        # Cela retient des triplets pour traitement ultérieur.
        if r == 0:
            s.append(set([x, y, z]))
        # Sinon (r != 0), on ajoute chacun des trois indices à l'ensemble 'c' (nécessairement pas de doublons dans un set).
        else:
            c.add(x)
            c.add(y)
            c.add(z)

    # Début d'une boucle qui se poursuit indéfiniment, mais elle sera brisée après stabilisation d'une condition (voir plus bas).
    while True:
        # On pose un flag (un simple booléen) à True pour vérifier en fin de boucle si quelque chose a changé.
        f = True

        # On parcourt chaque élément de la liste 's'. Chacun de ces éléments est un ensemble de trois entiers.
        for lst in s:
            # On calcule l'intersection entre l'ensemble 'lst' et l'ensemble 'c' (donc : les éléments communs aux deux).
            # Si au moins 2 éléments sont communs, on va agir sur l'ensemble (~propagation, réduction).
            if len(lst & c) >= 2:
                # On retire (supprime) 'lst' de la liste 's' car il est traité.
                s.remove(lst)
                # On enlève à 'lst' tous les éléments qui appartiennent aussi à l'ensemble 'c'.
                lst = lst - c
                # S'il reste au moins 1 élément dans 'lst', on va déplacer cet unique élément (avec pop()) dans 'b'.
                # Cela identifie ici un index que l'on doit marquer comme 'b'.
                if len(lst) >= 1:
                    b.add(lst.pop())
                # On signale qu'il s'est passé quelque chose dans cette itération (on continue la boucle tant qu'il y a des changements).
                f = False
        # Si aucun changement dans la boucle précédente (f toujours égale à True), on casse la boucle while.
        if f:
            break

    # Après ces manipulations, on retire du set 'a' tous ceux qui sont dans 'b', puis aussi ceux qui sont dans 'c'.
    # 'a' contiendra alors uniquement les indices n'appartenant à 'b' ni à 'c'.
    a = a - b
    a = a - c

    # Parcours entier de 0 à n-1. On affiche, pour chaque indice, un nombre selon qu'il est dans 'a', 'b' ou 'c'.
    for i in range(n):
        # Si l'indice courant 'i' est dans 'a', on imprime 2.
        if i in a:
            print 2
        # Sinon, s'il appartient à 'b', on imprime 0.
        elif i in b:
            print 0
        # Sinon, il est implicitement dans 'c', on imprime donc 1.
        else:
            print 1
# Boucle infinie : la boucle 'while True:' va tourner indéfiniment jusqu'à ce qu'une instruction 'break' soit rencontrée à l'intérieur de la boucle.
while True:
    # On demande à l'utilisateur d'entrer une valeur. La fonction 'input()' attend que l'utilisateur tape quelque chose au clavier puis appuie sur Entrée.
    n = input()
    # Ici, on compare la valeur saisie à 0.
    # Cependant, la fonction input() retourne une chaîne de caractères, il faut donc la convertir en entier pour faire une comparaison correcte avec le nombre 0.
    # Si la condition est vraie (c'est-à-dire que l'utilisateur a entré 0), alors on utilise 'break' pour sortir de la boucle infinie.
    if int(n) == 0:
        break

    # La boucle suivante sert à répéter un certain nombre de fois, précisé par l'utilisateur en entrerant n.
    # 'range(n)' génère une séquence de nombres entiers de 0 à n-1.
    # Chaque valeur de cette séquence sera successivement affectée à la variable 'i' durant chaque itération de la boucle.
    # Cela signifie que la boucle tournera exactement 'n' fois.
    for i in range(int(n)):
        # Demander à l'utilisateur de saisir trois entiers (pm, pe, pj) sur la même ligne, séparés par des espaces.
        # 'raw_input()' lit toute la ligne entrée par l'utilisateur (fonctionne en Python 2, en Python 3 'input()' doit être utilisé à la place).
        # 'split()' divise la chaîne en une liste de sous-chaînes, en séparant là où il y a des espaces.
        # 'map(int, ...)': applique la fonction int() à chaque sous-chaîne pour les convertir en entiers.
        # Les trois entiers sont ensuite simultanément affectés aux variables pm, pe, pj.
        pm, pe, pj = map(int, raw_input().split())

        # Calculer la moyenne arithmétique simple des trois notes, en additionnant pm, pe et pj, puis en divisant le total par 3.0 pour conserver la division réelle (à virgule flottante).
        ave = (pm + pe + pj) / 3.0

        # Ici, on procède à des tests pour déterminer la note finale parmi 'A', 'B', ou 'C'.
        # Première condition (grade 'A'):
        # - Si l'une quelconque des trois notes (pm, pe, pj) est égale à 100, la note finale est 'A' (on utilise l'opérateur 'in' pour vérifier la présence de 100 dans la collection (pm, pe, pj)).
        # - OU si la moyenne simple de pm et pe (donc (pm + pe)/2) est supérieure ou égale à 90, on obtient aussi 'A'.
        # - OU enfin, si la moyenne globale 'ave' est au moins 80, c'est aussi un 'A'.
        if (100 in (pm, pe, pj)) or ((pm + pe) / 2 >= 90) or (ave >= 80):
            # Si une des conditions précédentes est vraie, afficher 'A'.
            print "A"
        # Deuxième condition (grade 'B'):
        # - Si la moyenne générale 'ave' est supérieure ou égale à 70, la note sera B.
        # - OU, si la moyenne générale est au moins 50, ET (c'est-à-dire que dans ce cas on utilise 'and') au moins une des deux notes pm ou pe vaut 80 ou plus, la note est aussi B.
        elif (ave >= 70) or ((ave >= 50) and ((pm >= 80) or (pe >= 80))):
            # Afficher 'B' si une des conditions ci-dessus est satisfaite.
            print "B"
        # Si aucune des conditions précédentes n'est satisfaite, alors la note sera 'C'.
        else:
            print "C"
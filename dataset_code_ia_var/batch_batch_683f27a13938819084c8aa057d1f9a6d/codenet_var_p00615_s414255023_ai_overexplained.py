# Commence une boucle infinie qui devra être interrompue manuellement par une instruction de sortie explicite
while True:

    # Lit une ligne à partir de l'entrée standard avec raw_input(), qui renvoie une chaîne de caractères
    # split() décompose cette chaîne selon les espaces, donnant une liste de chaînes
    # map(int, ...) convertit chaque chaîne en entier
    # L'affectation multiple permet d'attribuer simultanément les deux premiers entiers à n et m
    n, m = map(int, raw_input().split())

    # Vérifie si n vaut 0 ET m vaut 0, ce qui indique la condition d'arrêt
    # Si cette condition est vraie, la boucle se termine grâce à break
    if n == m == 0:
        break

    # Si n n'est pas 0, on lit la liste des éléments "up" depuis l'entrée
    # raw_input() lit une ligne, split() la découpe, map(int, ...) convertit chaque élément en entier
    # Si n vaut 0, on affecte une liste vide à up car il n'y a rien à lire
    up = map(int, raw_input().split()) if n != 0 else []

    # Même logique que pour "up" mais pour m et pour la liste "down"
    down = map(int, raw_input().split()) if m != 0 else []

    # Fusionne les deux listes "up" et "down" dans une seule liste "upDown"
    upDown = up + down

    # Trie la liste "upDown" dans l'ordre croissant, permettant un traitement par différence de voisins
    upDown.sort()

    # Initialise la variable maxlen avec la première valeur de la liste triée
    # Cela sert de point de départ pour la comparaison ultérieure
    maxlen = upDown[0]

    # Boucle sur tous les indices de 0 jusqu'à n+m-2 (inclus), car range(n+m-1) s'arrête avant n+m-1
    # Cela permet de comparer chaque élément à son suivant dans la liste triée
    for i in range(n + m - 1):
        # Calcule la différence entre l'élément i+1 et l'élément i, représente l'écart entre deux valeurs consécutives
        # Compare cette différence avec la valeur courante de maxlen et affecte la plus grande à maxlen
        maxlen = max(maxlen, upDown[i + 1] - upDown[i])

    # Affiche la valeur finale de maxlen après traitement de tous les écarts
    print maxlen
# Début d'une boucle boucle infinie, c'est-à-dire qu'elle s'exécutera indéfiniment jusqu'à ce qu'on rencontre une instruction de sortie explicite comme 'break'
while True:
    # Lit une ligne au clavier, divise la chaîne selon les espaces, convertit les éléments en entiers et les affecte à n et m
    n, m = map(int, raw_input().split())

    # Si les deux valeurs n ET m sont toutes les deux nulles, on sort de la boucle grâce à 'break'
    if n == 0 and m == 0:
        break

    # Initialisation d'une liste nommée 'traffic' qui contiendra tous les éléments qu'on va traiter
    # On place un zéro dans la liste pour commencer (cela représente possiblement le point de départ)
    traffic = [0]

    # Si n n'est pas nul (donc il y a des valeurs à lire pour la première catégorie d'entrées)
    if n != 0:
        # On lit la ligne suivante depuis l'entrée standard, on la divise en parties selon les espaces,
        # puis on convertit chacune des chaînes de caractères en entier.
        # On met le résultat dans 'traffic', remplaçant son contenu actuel
        traffic = map(int, raw_input().split())

    # Si m n'est pas nul (donc il y a des valeurs pour la deuxième catégorie d'entrées)
    if m != 0:
        # On lit la ligne suivante, on la divise par espaces, on convertit chaque part en entier,
        # puis on AJOUTE ces nouveaux entiers à la liste existante 'traffic' grâce à l'opérateur +=
        traffic += map(int, raw_input().split())

    # On trie la liste 'traffic' en place (c'est-à-dire qu'elle sera ordonnée croissante)
    traffic.sort()

    # On initialise une variable 'max' à la première valeur de la liste 'traffic',
    # Cela va servir à garder trace du plus grand écart trouvé (on présume initialement le maximum est la première valeur)
    max = traffic[0]

    # On initialise une variable 'next' contenant également la première valeur de la liste traffic,
    # Cela va représenter la valeur précédente lors de l'itération à venir
    next = traffic[0]

    # On commence une boucle sur tous les éléments de la liste 'traffic' SAUF le premier (vu qu'il est déjà traité)
    for var in traffic[1:]:
        # Si la différence entre l'élément courant 'var' et la précédente valeur 'next'
        # est STRICTEMENT plus grande que la valeur de 'max', on réactualise 'max' avec ce nouvel écart
        if var - next > max:
            max = var - next
        # On met à jour 'next' pour la prochaine itération : 'next' devient la valeur actuelle 'var'
        next = var

    # Lorsque la boucle a fini de comparer tous les écarts,
    # on affiche la valeur maximale trouvée, c'est-à-dire le plus grand écart
    print max
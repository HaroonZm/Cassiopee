# Commencer une boucle infinie qui s'exécutera tant que la condition True reste vraie.
while True:
    # Lire une ligne depuis l'entrée utilisateur, la séparer avec 'split()' (espaces par défaut), convertir chaque morceau en entier avec 'map(int, ...)',
    # puis construire une liste à partir du résultat avec 'list(...)'.
    # On assigne ensuite les trois valeurs à m, n_min et n_max, qui sont respectivement le nombre d'éléments à lire plus tard et deux bornes numériques.
    m, n_min, n_max = list(map(int, input().split()))
    
    # Vérifier si la valeur de 'm' est égale à zéro.
    # Si c'est le cas, cela signifie que l'on veut arrêter le programme.
    if m == 0:
        # Sortir de la boucle while. Cela mettra fin au programme.
        break
    
    # Créer une liste 'v' contenant 'm' entiers, chacun étant fourni par l'utilisateur à chaque itération.
    # On utilise une compréhension de liste : on répète la lecture et la conversion 'm' fois dans une boucle.
    v = [int(input()) for _ in range(m)]
    
    # Initialiser 'max_gap' avec la valeur zéro.
    # Cette variable contiendra la plus grande différence trouvée jusqu'à présent lors de la suite des comparaisons.
    max_gap = 0
    
    # Initialiser 'max_index' avec la valeur de 'n_min'.
    # Cette variable gardera l'indice (plus précisément la position) pour lequel on aura observé un écart maximal.
    max_index = n_min

    # Démarrer une boucle 'for' allant de 'n_min' jusqu'à 'n_max' inclusivement.
    # range(a, b+1) va de a à b inclus, car la borne supérieure en python est exclusive.
    for i in range(n_min, n_max + 1):
        # Calculer la différence entre 'v[i-1]' et 'v[i]'.
        # 'i-1' est utilisé car la plupart des indices en Python commencent à zéro, mais ici 'i' commence à 'n_min'.
        # On cherche donc l'écart entre deux éléments consécutifs d'indice (i-1) et i.
        gap = v[i - 1] - v[i]
        
        # On vérifie si le nouvel écart ('gap') trouvé est supérieur à l'écart maximum précédent.
        if gap > max_gap:
            # Si oui, on met à jour 'max_gap' avec la nouvelle plus grande valeur trouvée.
            max_gap = gap
            # On met également à jour 'max_index' avec la position correspondante 'i'.
            max_index = i
        # Si l'écart actuel est égal à l'écart maximum déjà enregistré (cas d'égalité),
        # on décide de mettre à jour malgré tout l'indice.
        elif gap == max_gap:
            # On met à jour 'max_index' avec la valeur courante de 'i'.
            max_index = i
    
    # Une fois toutes les comparaisons terminées, afficher la valeur de 'max_index'.
    # Ceci indiquera l'indice correspondant à la plus grande différence trouvée (ou la dernière en cas d'ex-aequo).
    print(max_index)
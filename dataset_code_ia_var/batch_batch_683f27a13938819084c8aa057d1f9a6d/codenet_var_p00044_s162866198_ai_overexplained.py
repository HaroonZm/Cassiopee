# Création d'une liste 'lst' contenant 50021 éléments, initialisés à la valeur 1.
# Ici, l'opérateur * répète la liste [1] 50021 fois pour en faire une grande liste.
lst = [1] * 50021

# Boucle for qui va parcourir tous les indices de 0 jusqu'à 50020 inclus (car range(50021) exclut la borne supérieure).
for i in range(50021):
    # Si l'indice en cours (i) est égal à 0, alors...
    if i == 0:
        # On remet la valeur de lst[0] à 0 (donc le premier élément de la liste).
        lst[i] = 0
    else:
        # Sinon, si la valeur actuelle de lst[i] vaut 1 (on vérifie seulement les positions qui n'ont pas été modifiées)...
        if lst[i] == 1:
            # On définit une nouvelle variable j comme étant l'indice suivant (i + 1).
            j = i + 1
            # La variable k reçoit la valeur actuelle de l'indice i.
            k = i
            # On rentre dans une boucle infinie qui permet d'atteindre et de modifier certains indices multiples.
            while True:
                # On incrémente k de la valeur de j (k = k + j).
                k = k + j
                # Si k est supérieur ou égal à 50021 (c'est-à-dire en dehors des bornes valides de la liste)... 
                if k >= 50021:
                    # ... on sort de la boucle infinie grâce au mot-clé break.
                    break
                # Sinon, on met la valeur 0 à l'emplacement k dans la liste lst (lst[k] = 0). 
                # Cela signifie, dans ce contexte, qu'on marque les multiples de j (candidats à exclure comme dans le Crible d'Ératosthène).

# On entre dans une boucle infinie pour traiter plusieurs entrées consécutives sans redémarrer le programme.
while True:
    try:
        # On essaie de lire une entrée de l'utilisateur via la fonction input().
        # Par défaut, input() renvoie une chaîne de caractères, donc on la convertit en entier avec int().
        n = int(input())
        # On prend une sous-liste 'a' qui correspond à tous les éléments de lst depuis l'indice 0 jusqu'à n-2 inclus (attention : l'indice de fin est exclu).
        a = lst[0:n-1]
        # On prend une sous-liste 'b' qui correspond à tous les éléments de lst à partir de l'indice n jusqu'à la fin de la liste.
        b = lst[n:]
        # Pour trouver le nombre premier immédiatement inférieur à n, on procède :
        # On inverse la sous-liste 'a' avec [::-1], ce qui la parcourt à l'envers.
        # On cherche la première occurrence de la valeur 1 grâce à index(1), ce qui donne la distance depuis n-2 vers 0 du plus grand indice de 1.
        # On le retranche de n-1 afin d’obtenir son indice réel dans lst. 
        left = n - 1 - a[::-1].index(1)
        # Pour trouver le nombre premier immédiatement supérieur à n :
        # On cherche dans 'b' la première occurrence de 1 grâce à index(1) (distance depuis n).
        # On additionne n+1 à la distance trouvée car lst[n:] commence à l'indice n, donc on ajoute aussi 1 pour trouver la vraie valeur.
        right = n + 1 + b.index(1)
        # On affiche les deux indices calculés, séparés par un espace, grâce à la fonction print, sous forme de tuple.
        print(left, right)
    # Si une erreur EOFError survient (ce qui arrive lorsqu'on atteint la fin de fichier ou que l'utilisateur n'entre plus d'input)...
    except EOFError:
        # ... alors on sort de la boucle infinie avec break. Le programme s'arrête alors proprement.
        break
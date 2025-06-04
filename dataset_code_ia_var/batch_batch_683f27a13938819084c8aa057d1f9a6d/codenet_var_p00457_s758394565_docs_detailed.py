INF = 100000

while True:
    # Lecture du nombre d'éléments dans la séquence
    n = int(input())
    if not n:
        # Sort de la boucle principale si l'entrée est 0
        break

    # Lecture de la séquence de n entiers, supposée valoir 1, 2 ou 3 pour chaque élément
    lst = [int(input()) for _ in range(n)]

    def check(x):
        """
        Calcule la taille minimale de la séquence après des suppressions successives,
        en commençant par une modification à la position x.

        Suppression successive :
        Si une zone (contiguë) d'au moins trois éléments consécutifs de même valeur se forme,
        elle est supprimée, et on répète le processus tant que possible.

        Args:
            x (int): La position dans la liste à laquelle on a effectué un changement.

        Returns:
            int: La taille résiduelle minimale de la séquence après l'ensemble des suppressions.
        """
        # Valeurs initiales utilisées pour l'expansion autour de x
        c1 = c2 = lst[x]  # Valeur initiale à la position modifiée
        l = r = x         # Indices gauche (l) et droite (r) de la plage homogène
        b = 0             # Nombre d'éléments supprimés jusqu'ici (taille du bloc)

        # Déterminer l'extension à droite pour obtenir le plus long segment identique à partir de x
        for i in range(r, n):
            if lst[i] != c2:
                r = i - 1
                break
        else:
            r = n - 1  # Atteint la fin de la liste

        # Déterminer l'extension à gauche pour obtenir le plus long segment identique à partir de x
        for i in range(l, -1, -1):
            if lst[i] != c1:
                l = i + 1
                break
        else:
            l = 0  # Atteint le début de la liste

        # Si le bloc identifié n'est pas assez long pour être supprimé (moins de 3 éléments)
        if r - l - b < 3:
            return n  # Aucune suppression possible, retourner taille originale
        else:
            b = r - l  # Mettre à jour la taille du bloc supprimé

        # Essayer de "chaîner" les suppressions en agrandissant à gauche et à droite
        while l > 0 and r < n - 1:
            c1 = lst[l - 1]   # Valeur supplémentaire à gauche
            c2 = lst[r + 1]   # Valeur supplémentaire à droite

            if c1 != c2:
                # Chaînage impossible si les valeurs adjacentes diffèrent
                break
            else:
                # Étendre la zone homogène à droite s'il y a des valeurs identiques à c2
                for i in range(r + 1, n):
                    if lst[i] != c2:
                        r = i - 1
                        break
                else:
                    r = n - 1

                # Étendre la zone homogène à gauche s'il y a des valeurs identiques à c1
                for i in range(l - 1, -1, -1):
                    if lst[i] != c1:
                        l = i + 1
                        break
                else:
                    l = 0

                # Vérifier que la nouvelle région à supprimer est suffisante (au moins 4)
                if r - l - b < 4:
                    # Arrête l'enchaînement si la nouvelle fusion n'est pas assez grande
                    break
                else:
                    b = r - l  # Mettre à jour la taille du bloc supprimé

        # Retourne la longueur résiduelle après toutes les suppressions
        return n - (b + 1)

    ans = INF  # Initialisation de la réponse avec un grand nombre

    for i in range(n):
        # À chaque position i, essayer les trois transformations possibles
        # (les valeurs des éléments changent cycliquement entre 1, 2 et 3)
        
        # Premier essai de transformation
        lst[i] = (lst[i] + 1) % 3 + 1
        ans = min(ans, check(i))
        
        # Deuxième essai de transformation
        lst[i] = (lst[i] + 1) % 3 + 1
        ans = min(ans, check(i))
        
        # Restaure la valeur initiale pour ne pas impacter la suite de la boucle
        lst[i] = (lst[i] + 1) % 3 + 1

    # Affiche la taille minimale résiduelle trouvée pour cette séquence
    print(ans)
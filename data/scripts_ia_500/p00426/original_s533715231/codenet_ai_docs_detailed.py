def solve():
    """
    Lit plusieurs cas de figure depuis l'entrée standard, puis pour chacun,
    calcule et affiche un nombre minimal de déplacements nécessaires selon
    une règle définie.

    Le programme s'arrête lorsque la valeur de n lue est égale à 0.
    """

    from sys import stdin
    f_i = stdin

    def rec(i):
        """
        Fonction récursive calculant un nombre selon la configuration des gobelets.

        Args:
            i (int): Indice représentant le nombre d'éléments restant à considérer.

        Returns:
            int: Le résultat calculé selon les règles récursives et la liste 'cups'.
        """
        if i == 0:
            # Cas de base : pas d'éléments à traiter, retourne 0
            return 0
        
        tray = cups[n - i]  # Obtient le type de gobelet à la position courante

        if tray == 'A':
            # Si le gobelet est de type A, on continue la récursion sans modification
            return rec(i - 1)
        elif tray == 'B':
            # Si le gobelet est de type B, applique une formule combinant les puissances de 3
            # et le résultat récursif précédent, inversant certaines valeurs
            return 2 * 3 ** (i - 1) - 1 - rec(i - 1)
        else:
            # Si le gobelet est de type C, ajoute une valeur proportionnelle à la puissance de 3
            # au résultat récursif de l'étape précédente
            return rec(i - 1) + 2 * 3 ** (i - 1)

    while True:
        n, m = map(int, f_i.readline().split())
        # Sort de la boucle principale si n est nul
        if n == 0:
            break
        
        cups = [None] * n  # Initialise une liste destinée à contenir les types de gobelets

        # Pour chaque type de gobelet (A, B, C), on lit une ligne contenant des indices
        # On met à jour la liste des gobelets avec leur type respectif
        for tray in 'ABC':
            itr = map(int, f_i.readline().split())
            next(itr)  # Ignore le premier nombre qui donne le nombre d'éléments pour ce tray
            for i in itr:
                cups[i-1] = tray
        
        # Calcule un nombre en fonction de la configuration complète des gobelets
        num = rec(n)
        
        # Calcule le minimum entre ce nombre et son complémentaire relatif à 3^n - 1
        ans = min(num, 3 ** n - 1 - num)
        
        # Affiche la réponse si elle est inférieure ou égale à m, sinon -1
        if ans <= m:
            print(ans)
        else:
            print(-1)

solve()
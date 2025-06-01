while True:
    # Lecture des entrées correspondant au prix à atteindre (p) et au nombre de pièces disponibles pour chaque dénomination
    p, n1, n5, n10, n50, n100, n500 = map(int, input().split())
    
    # Condition d'arrêt : si le prix p est 0, on sort de la boucle infinie
    if p == 0:
        break
    
    # Définition des valeurs des pièces, triées de la plus grande à la plus petite
    values = (500, 100, 50, 10, 5, 1)
    # Correspondance du nombre de pièces disponibles pour chaque valeur
    values_cnt = (n500, n100, n50, n10, n5, n1)
    # Constante représentant une valeur "infinie" pour le cas où le rendu est impossible
    INF = 10 ** 20

    def return_cnt(x):
        """
        Calcule le nombre minimal de pièces nécessaires pour rendre la monnaie d'une somme donnée x,
        en supposant une disponibilité illimitée de chaque pièce de valeur selon 'values'.
        
        Args:
            x (int): Le montant dont on veut calculer le nombre minimal de pièces nécessaires.
            
        Returns:
            int: Le nombre minimal de pièces pour rendre le montant x.
        """
        ret = 0  # Initialisation du compteur de pièces
        for value in values:
            # On prend le maximum de pièces de la valeur actuelle pouvant être utilisées pour le reste x
            ret += x // value
            # On réduit x par la valeur rendue avec ces pièces
            x %= value
        return ret

    def make_price(x):
        """
        Calcule le nombre minimal de pièces nécessaires pour atteindre exactement le montant x,
        en tenant compte des quantités limitées de pièces disponibles dans 'values_cnt'.
        
        Args:
            x (int): Le montant à atteindre.
            
        Returns:
            int: Le nombre minimum de pièces utilisées pour atteindre x si possible,
                 sinon une valeur très élevée (INF) indiquant l'impossibilité.
        """
        ret = 0  # Compteur du nombre de pièces utilisées
        for value, cnt in zip(values, values_cnt):
            # Calcul du nombre maximal de pièces de cette valeur pouvant être utilisées sans dépasser x
            available_cnt = x // value
            # Prend le minimum entre ce qui est nécessaire et ce qui est disponible
            use = min(available_cnt, cnt)
            ret += use  # Ajoute ces pièces au total
            x -= value * use  # Réduit x du montant couvert par ces pièces
        if x == 0:  # Si on a atteint exactement x, on retourne le nombre total de pièces utilisées
            return ret
        return INF  # Sinon, on retourne une grande valeur indiquant que le rendu est impossible

    # Pour tous les montants i allant de p à p+499
    # on calcule la somme des pièces nécessaires pour réaliser exactement i (avec la contrainte des pièces disponibles)
    # plus les pièces nécessaires pour rendre la monnaie de (i - p) (avec disponibilité illimitée)
    # On affiche ensuite le minimum de ces sommes, correspondant au nombre minimal total de pièces à manipuler
    print(min([make_price(i) + return_cnt(i - p) for i in range(p, p + 500)]))
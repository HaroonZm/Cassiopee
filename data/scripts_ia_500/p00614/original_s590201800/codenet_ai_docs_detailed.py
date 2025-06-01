price = [1, 5, 10, 50, 100, 500]

def min_coins_for_payment_and_change(price, n, p):
    """
    Calcule le nombre minimal de pièces nécessaires pour effectuer un paiement d'un montant p,
    en utilisant une quantité donnée de pièces n de différentes valeurs, puis rendre la monnaie
    avec un nombre minimal de pièces.

    Args:
        price (list of int): Liste des valeurs des pièces disponibles.
        n (list of int): Quantité disponible pour chaque pièce, correspondant aux valeurs de price.
        p (int): Montant à payer.

    Returns:
        float: Nombre minimal total de pièces utilisées pour payer et rendre la monnaie,
               ou une très grande valeur si le paiement n'est pas possible avec les pièces données.
    """
    ans = 1e100  # Initialisation avec une valeur très élevée pour trouver le minimum

    # Calcul de la somme totale des pièces disponibles * leur valeur
    p_sum = sum(value * count for value, count in zip(price, n))

    # On essaie d'augmenter le paiement p par un certain changement 'change',
    # c'est-à-dire on paie p + change, puis on rend 'change' en monnaie
    for change in range(1000):
        total = p + change  # Montant total à payer avec la monnaie supplémentaire
        pay = [0] * 6      # Liste pour stocker le nombre de pièces utilisées pour payer

        # Tentative de constituer le paiement total avec les pièces disponibles, en privilégiant les plus grosses
        for i in reversed(range(6)):
            if total >= price[i]:
                # On prend autant que possible de pièces de cette valeur sans dépasser n[i]
                pay[i] = min(n[i], int(total / price[i]))
                total -= pay[i] * price[i]  # On réduit le total restant à payer

        # Si on n'a pas réussi à payer la totalité, on arrête la recherche pour cette valeur de 'change'
        if total > 0:
            break

        coins = sum(pay)  # Somme des pièces utilisées pour payer

        # Calcul du nombre de pièces nécessaires pour rendre la monnaie 'change'
        _change = change
        for i in reversed(range(6)):
            if _change >= price[i]:
                coins += int(_change / price[i])  # Ajouter les pièces pour rendre la monnaie
                _change %= price[i]                # Reste à rendre

        # Mise à jour du nombre minimal de pièces total utilisé
        ans = min(ans, coins)

    return ans


# Boucle principale du programme qui lit les entrées utilisateur
while True:
    # Lecture d'une ligne d'entrée contenant le montant à payer suivi du nombre de pièces disponibles
    values = list(map(int, input().split()))
    p, n = values[0], values[1:]  # p est le montant à payer, n la liste des pièces disponibles

    # Condition d'arrêt si le montant à payer est 0
    if p == 0:
        break

    # Calcul et affichage du résultat minimal obtenu avec la fonction dédiée
    result = min_coins_for_payment_and_change(price, n, p)
    print(result)
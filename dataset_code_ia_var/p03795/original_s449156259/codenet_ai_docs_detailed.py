n = int(input())

def main(n):
    """
    Calcule le coût total en fonction de la quantité n.
    Pour chaque tranche de 15 unités achetées, une réduction de 200 est appliquée.

    Args:
        n (int): Le nombre d'articles achetés.

    Returns:
        int: Le montant total à payer après application de la réduction.
    """
    # Calcul du nombre de tranches de 15 unités et de la réduction totale à appliquer
    reduction = (n // 15) * 200

    # Calcul du montant total sans réduction
    total = n * 800

    # Retourne le montant total à payer après réduction
    return total - reduction

# Appelle la fonction main avec l'entrée de l'utilisateur et stocke la réponse
ans = main(n)

# Affiche la réponse finale
print(ans)
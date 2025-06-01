def calculate_best_price(x, y, b, p):
    """
    Calcule le prix optimal en fonction des quantités achetées et des conditions de réduction.

    Args:
        x (int): Prix unitaire du premier produit.
        y (int): Prix unitaire du second produit.
        b (int): Quantité achetée du premier produit.
        p (int): Quantité achetée du second produit.

    Returns:
        int: Le prix à payer après application éventuelle d'une réduction selon les règles définies.
    """
    # Calcul du prix régulier sans aucune modification des quantités
    regular_price = x * b + y * p

    # Si les quantités sont déjà au moins 5 pour b et 2 pour p, appliquer directement la réduction de 20%
    if b >= 5 and p >= 2:
        # Calcul du prix avec réduction 20%
        discounted_price = int(regular_price * 0.8)
        return discounted_price
    else:
        # Sinon, ajuster les quantités pour atteindre les seuils minimums correspondant aux conditions de réduction
        adjusted_b = b if b >= 5 else 5
        adjusted_p = p if p >= 2 else 2

        # Calcul du prix réduit avec les quantités ajustées
        discounted_price = int((x * adjusted_b + y * adjusted_p) * 0.8)

        # Comparer le prix régulier (avec quantités initiales) et le prix réduit (avec quantités ajustées)
        # Retourner le moins cher des deux
        if regular_price <= discounted_price:
            return regular_price
        else:
            return discounted_price


def main():
    """
    Fonction principale pour lire les entrées, appliquer le calcul du prix optimal et afficher les résultats.
    """
    # Lire le nombre de cas de test
    N = int(input())

    # Pour chaque cas, lire les paramètres, calculer et afficher le prix optimal
    for _ in range(N):
        # Lire les 4 entiers séparés par un espace
        x, y, b, p = map(int, input().split())
        # Calculer le prix optimal avec la fonction dédiée
        best_price = calculate_best_price(x, y, b, p)
        # Afficher le résultat
        print(best_price)


if __name__ == "__main__":
    main()
def calculate_total_price(number_of_items):
    """
    Calcule le prix total pour un nombre donné d'articles,
    en appliquant une réduction pour chaque tranche de 15 articles.

    Args:
        number_of_items (int): Le nombre total d'articles achetés.

    Returns:
        int: Le prix total après application de la réduction.
    """
    # Prix unitaire de chaque article
    unit_price = 800
    # Réduction appliquée pour chaque tranche de 15 articles
    discount_per_15_items = 200

    # Calcul du prix sans réduction
    total_price = number_of_items * unit_price

    # Calcul du nombre de réductions applicables (tranches de 15 articles)
    discount_count = number_of_items // 15

    # Calcul du montant total de la réduction
    total_discount = discount_count * discount_per_15_items

    # Calcul du prix final après application de la réduction
    final_price = total_price - total_discount

    return final_price

if __name__ == "__main__":
    # Lecture de l'entrée utilisateur pour obtenir le nombre d'articles
    n = int(input("Entrez le nombre d'articles : "))

    # Calcul du prix total avec les remises
    result = calculate_total_price(n)

    # Affichage du prix total à l'utilisateur
    print(result)
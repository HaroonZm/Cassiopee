def calculate_lunch_total(n):
    """
    Calcule le coût total des déjeuners d'entreprise.

    La formule utilisée est :
        total = 800 * n - 200 * (n // 15)
    où :
        - 800 est le coût d'un déjeuner (en yens)
        - n est le nombre de déjeuners achetés
        - pour chaque tranche de 15 déjeuners achetés, une réduction de 200 yens est appliquée

    Args:
        n (int): Le nombre de déjeuners achetés.

    Returns:
        int: Le coût total après application de la réduction.
    """
    # Calcul du total sans réduction
    total_without_discount = 800 * n
    # Calcul du nombre de réductions à appliquer
    discount_count = n // 15
    # Calcul du montant total de la réduction
    total_discount = 200 * discount_count
    # Calcul du total final après réduction
    total = total_without_discount - total_discount
    return total

if __name__ == "__main__":
    # Lecture de l'entrée utilisateur pour le nombre de déjeuners
    n = int(input())
    # Calcul et affichage du montant total
    print(calculate_lunch_total(n))
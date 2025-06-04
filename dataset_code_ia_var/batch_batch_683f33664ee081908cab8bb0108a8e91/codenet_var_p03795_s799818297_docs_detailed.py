def calculate_total_cost(n):
    """
    Calcule le coût total basé sur le nombre d'articles commandés.
    
    Chaque article coûte 800 unités. Pour chaque tranche complète de 15 articles,
    une réduction de 200 unités est appliquée.

    Args:
        n (int): Le nombre d'articles commandés.

    Returns:
        int: Le coût total après application des réductions.
    """
    # Calculer le coût sans réduction
    total_cost = 800 * n

    # Calculer le nombre de réductions applicables (une tous les 15 articles)
    num_discounts = n // 15

    # Calculer le montant total de la réduction
    total_discount = 200 * num_discounts

    # Calculer le coût final après réduction
    final_cost = total_cost - total_discount

    return final_cost

if __name__ == "__main__":
    # Demander à l'utilisateur d'entrer le nombre d'articles commandés
    n = int(input())

    # Calculer le coût total avec la fonction définie
    result = calculate_total_cost(n)

    # Afficher le coût total
    print(result)
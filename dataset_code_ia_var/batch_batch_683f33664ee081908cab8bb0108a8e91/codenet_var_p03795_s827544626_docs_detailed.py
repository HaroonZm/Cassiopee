def calculate_total_cost(n):
    """
    Calcule le coût total après avoir appliqué une réduction basée sur le nombre d'articles achetés.

    La fonction calcule le coût pour 'n' articles, chaque article coûtant 800.
    Pour chaque groupe de 15 articles achetés, une réduction de 200 est appliquée.

    Args:
        n (int): Le nombre d'articles achetés.

    Returns:
        int: Le coût total après la réduction.
    """
    # Coût total sans réduction, chaque article coûtant 800
    total_without_discount = 800 * n

    # Calcul du nombre de groupes de 15 articles
    discount_groups = n // 15

    # Calcul du montant total de la réduction (200 par groupe de 15)
    total_discount = 200 * discount_groups

    # Coût total après application de la réduction
    total_with_discount = total_without_discount - total_discount

    return total_with_discount

def main():
    """
    Point d'entrée principal du programme.
    Demande à l'utilisateur d'entrer le nombre d'articles souhaité, 
    effectue le calcul du coût et affiche le résultat.
    """
    # Lecture du nombre d'articles depuis l'entrée standard et conversion en entier
    n = int(input())

    # Calcul du coût total en appelant la fonction dédiée
    ans = calculate_total_cost(n)

    # Affichage du résultat final
    print(ans)

# Appel du point d'entrée principal
if __name__ == "__main__":
    main()
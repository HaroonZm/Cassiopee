def calculate_minimum_cost(N, A, B):
    """
    Calcule le coût minimum entre deux options :
    1. Payer A unités pour chacun des N éléments.
    2. Payer un coût forfaitaire B pour l'ensemble.
    
    Args:
        N (int): Nombre d'éléments à acheter.
        A (int): Coût unitaire d'un élément.
        B (int): Coût global forfaitaire pour tous les éléments.

    Returns:
        int: Le coût minimum entre les deux options.
    """
    # Calcul du coût si l'on paie chaque élément séparément
    cost_option_1 = A * N
    
    # Le coût forfaitaire donné
    cost_option_2 = B
    
    # Retourne le minimum des deux options de coût
    return min(cost_option_1, cost_option_2)

if __name__ == "__main__":
    # Lecture des entrées utilisateur sous la forme de trois entiers séparés par des espaces
    N, A, B = map(int, input().split())
    
    # Calcul du coût minimum avec les valeurs fournies
    result = calculate_minimum_cost(N, A, B)
    
    # Affichage du résultat final
    print(result)
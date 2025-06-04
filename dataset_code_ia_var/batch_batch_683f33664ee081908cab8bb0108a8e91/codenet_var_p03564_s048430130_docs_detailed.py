def calculate_minimum_value(n, k):
    """
    Calcule la valeur minimale obtenue après n étapes, 
    en doublant ou en ajoutant k à chaque étape, 
    tout en conservant toujours la plus petite valeur possible.

    Args:
        n (int): Le nombre d'opérations à effectuer.
        k (int): Le nombre à ajouter à chaque itération.

    Returns:
        int: La valeur minimale obtenue après n étapes.
    """
    x = 1  # Initialisation de la variable x avec la valeur de départ
    for i in range(n):
        # À chaque étape, x prend la plus petite valeur entre son double et lui-même augmenté de k
        x = min(x * 2, x + k)
    return x

if __name__ == "__main__":
    # Lecture des entrées utilisateur pour n et k
    n = int(input("Entrez le nombre d'opérations (n) : "))
    k = int(input("Entrez la valeur à additionner (k) : "))

    # Calcul du résultat et affichage
    result = calculate_minimum_value(n, k)
    print(result)
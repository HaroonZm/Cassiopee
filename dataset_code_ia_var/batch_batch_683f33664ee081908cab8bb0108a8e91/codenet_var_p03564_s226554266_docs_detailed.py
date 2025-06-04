def compute_final_value(N: int, K: int) -> int:
    """
    Calcule la valeur finale après N itérations où, à chaque étape,
    on ajoute la valeur de 'val' ou K, selon la moindre des deux, à la variable 'val'.

    Args:
        N (int): Le nombre d'itérations à réaliser.
        K (int): La borne supérieure pour l'incrémentation de 'val'.

    Returns:
        int: La valeur finale après toutes les itérations.
    """
    val = 1  # Initialisation de la variable 'val' à 1

    # On parcourt chaque itération (un total de N fois)
    for i in range(N):
        # À chaque itération, on ajoute à 'val' le minimum entre la valeur courante de 'val' et K
        val += min(val, K)

    # Après les N itérations, on retourne la valeur finale de 'val'
    return val

if __name__ == "__main__":
    # Lecture du nombre d'itérations depuis l'entrée standard
    N = int(input())
    # Lecture de la borne supérieure depuis l'entrée standard
    K = int(input())
    # Calcul et affichage du résultat final
    print(compute_final_value(N, K))
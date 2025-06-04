def calculate_utilities(A: int, B: int, C: int) -> int:
    """
    Calcule le nombre maximum d'utilisations d'un service coûtant A unités,
    en partant d'un budget initial B, sans dépasser un nombre limite d'utilités C.

    Args:
        A (int): Le coût d'une utilisation.
        B (int): Le montant d'argent initial disponible.
        C (int): Le nombre maximum d'utilisations autorisé.

    Returns:
        int: Le nombre d'utilisations effectuées.
    """
    # Initialisation de la variable pour suivre le nombre d'utilisations restantes d'argent
    money = B
    # Initialisation du compteur d'utilités réalisées
    utility = 0

    # Si le coût d'une utilisation est supérieur au budget, aucune utilisation n'est possible
    if A > B:
        return utility
    else:
        # Boucle s'exécutant tant que le nombre d'utilisations ne dépasse pas la limite C
        # et que l'argent restant permet d'effectuer au moins une utilisation
        while (utility < C) and (money - A >= 0):
            # Incrémente le nombre d'utilisations
            utility += 1
            # Déduit le coût d'une utilisation du budget restant
            money -= A
        return utility

def main():
    """
    Fonction principale qui lit l'entrée utilisateur,
    appelle la fonction de calcul, et affiche le résultat.
    """
    # Demande à l'utilisateur de saisir trois entiers séparés par des espaces
    A, B, C = map(int, input().split())
    # Calcule le nombre maximal d'utilisations autorisées et l'affiche
    result = calculate_utilities(A, B, C)
    print(result)

if __name__ == "__main__":
    main()
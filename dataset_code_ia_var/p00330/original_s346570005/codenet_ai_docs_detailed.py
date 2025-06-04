def calculate_weight_multiple(weight):
    """
    Calcule le produit d'un entier 'weight' par 32.

    Args:
        weight (int): La valeur entière à multiplier.

    Returns:
        int: Le résultat de la multiplication de 'weight' par 32.
    """
    return weight * 32

def main():
    """
    Fonction principale du programme.
    Demande à l'utilisateur de saisir un nombre entier, puis
    affiche le résultat de la multiplication de ce nombre par 32.
    """
    # Demande à l'utilisateur de saisir un entier et convertit la saisie en int
    W = int(input("Veuillez saisir un nombre entier : "))
    # Calcule le résultat de la multiplication
    result = calculate_weight_multiple(W)
    # Affiche le résultat à l'écran
    print(result)

# Exécute la fonction principale si le script est lancé directement
if __name__ == "__main__":
    main()
def read_input():
    """
    Lit une ligne de l'entrée standard, sépare la ligne en deux entiers et les retourne.

    Returns:
        tuple: Un tuple contenant deux entiers (A, B) extraits de l'entrée utilisateur.
    """
    # Lire la ligne de l'utilisateur, séparer par espaces, convertir chaque partie en int
    A, B = list(map(int, input().split()))
    return A, B

def compute_max_operation(A, B):
    """
    Calcule et retourne la valeur maximale parmi la somme, la différence et le produit de A et B.

    Args:
        A (int): Premier entier.
        B (int): Deuxième entier.

    Returns:
        int: La plus grande valeur parmi A+B, A-B et A*B.
    """
    # Calculer toutes les opérations possibles
    addition = A + B
    soustraction = A - B
    multiplication = A * B
    # Retourner la plus grande valeur parmi les trois
    return max(addition, soustraction, multiplication)

def main():
    """
    Fonction principale du programme qui orchestre la lecture des données,
    le calcul du résultat et son affichage.
    """
    # Lire les deux entiers depuis l'entrée utilisateur
    A, B = read_input()
    # Calculer la valeur maximale parmi toutes les opérations
    maximum = compute_max_operation(A, B)
    # Afficher le résultat à l'utilisateur
    print(maximum)

# Exécuter la fonction principale si ce fichier est exécuté comme script principal
if __name__ == "__main__":
    main()
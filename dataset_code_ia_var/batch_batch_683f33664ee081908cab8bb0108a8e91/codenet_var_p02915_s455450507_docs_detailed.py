def compute_cube(n):
    """
    Calcule le cube d'un nombre entier.
    
    Args:
        n (int): Le nombre entier dont on souhaite calculer le cube.
    
    Returns:
        int: Le cube de n (n*n*n).
    """
    return n * n * n

def main():
    """
    Fonction principale du programme. Elle demande à l'utilisateur de saisir un entier,
    puis affiche le cube de cet entier.
    """
    # Demande à l'utilisateur de saisir un nombre entier
    n = int(input("Entrez un entier : "))
    
    # Calcule le cube de l'entier grâce à la fonction compute_cube
    result = compute_cube(n)
    
    # Affiche le résultat
    print(result)

# Appel de la fonction principale pour exécuter le programme
if __name__ == "__main__":
    main()
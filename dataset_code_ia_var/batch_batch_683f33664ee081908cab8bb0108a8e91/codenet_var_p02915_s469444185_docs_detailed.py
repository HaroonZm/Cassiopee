def main():
    """
    Fonction principale qui exécute le programme :
    Demande à l'utilisateur d'entrer un entier, puis affiche son cube.
    """
    # Demander à l'utilisateur de saisir un entier
    a = get_user_input()
    
    # Calculer le cube et afficher le résultat
    result = cube(a)
    print(result)

def get_user_input():
    """
    Demande à l'utilisateur d'entrer un nombre entier via la fonction input.

    Returns:
        int: Le nombre entier saisi par l'utilisateur.
    """
    # Utilisation de input() pour lire une chaîne depuis le terminal,
    # puis conversion explicite de la chaîne en entier avec int().
    return int(input("Entrez un nombre entier : "))

def cube(n):
    """
    Calcule le cube d'un nombre entier donné.

    Args:
        n (int): Le nombre à mettre au cube.

    Returns:
        int: Le résultat de n élevé à la puissance 3.
    """
    return n * n * n

# Exécution du script si appelé directement
if __name__ == "__main__":
    main()
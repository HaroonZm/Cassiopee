def calculate_difference_of_square_and_value(n: int, a: int) -> int:
    """
    Calcule la différence entre le carré d'un nombre et une valeur donnée.

    Args:
        n (int): Le nombre à mettre au carré.
        a (int): La valeur à soustraire du carré de n.

    Returns:
        int: La différence entre n au carré et a.
    """
    # Calculer le carré de n
    square = n * n
    # Soustraire la valeur a du carré
    result = square - a
    # Retourner le résultat final
    return result

def main():
    """
    Fonction principale du programme.
    Demande à l'utilisateur de saisir deux entiers, 
    puis affiche la différence entre le carré du premier 
    entier et le second entier.
    """
    # Lecture de la première entrée utilisateur et conversion en entier
    n = int(input("Entrez un entier n : "))
    # Lecture de la deuxième entrée utilisateur et conversion en entier
    a = int(input("Entrez un entier a : "))
    # Calcul de la différence et affichage du résultat
    print(calculate_difference_of_square_and_value(n, a))

# Point d'entrée du script
if __name__ == "__main__":
    main()
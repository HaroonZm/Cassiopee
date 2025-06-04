import numpy as np

def calculate_difference_of_squares(n: int, a: int) -> int:
    """
    Calcule la différence entre le carré de n et la valeur de a.
    
    Paramètres :
    ----------
    n : int
        Un entier dont le carré sera calculé.
    a : int
        Un entier à soustraire du carré de n.
    
    Retourne :
    -------
    int
        La différence entre n*n et a.
    """
    # Calcul du carré de n
    square_of_n = n * n
    # Soustraction de a au carré de n
    difference = square_of_n - a
    # Renvoie de la différence calculée
    return difference

def main():
    """
    Fonction principale pour exécuter la logique de l'application.
    Demande à l'utilisateur deux entiers et affiche la différence entre le carré du premier entier et le second entier.
    """
    # Saisie de l'utilisateur pour le premier entier
    n = int(input("Entrez un entier n : "))
    # Saisie de l'utilisateur pour le second entier
    a = int(input("Entrez un entier a : "))
    # Calcul de la différence à l'aide de la fonction dédiée
    result = calculate_difference_of_squares(n, a)
    # Affichage du résultat à l'utilisateur
    print(result)

# Exécute la fonction principale si le script est lancé directement
if __name__ == "__main__":
    main()
def read_input():
    """
    Demande à l'utilisateur de saisir trois entiers représentant les deux bases et la hauteur d'un trapèze.
    
    Returns:
        tuple: Un triplet d'entiers (a, b, h) correspondant aux valeurs saisies par l'utilisateur.
    """
    # Lecture du premier entier : la première base du trapèze
    a = int(input("Entrez la première base du trapèze (a) : "))
    # Lecture du deuxième entier : la seconde base du trapèze
    b = int(input("Entrez la deuxième base du trapèze (b) : "))
    # Lecture du troisième entier : la hauteur du trapèze
    h = int(input("Entrez la hauteur du trapèze (h) : "))
    return a, b, h

def trapezoid_area(a, b, h):
    """
    Calcule l'aire d'un trapèze à partir de ses deux bases et de sa hauteur.
    
    Args:
        a (int): Longueur de la première base du trapèze.
        b (int): Longueur de la deuxième base du trapèze.
        h (int): Hauteur du trapèze.
        
    Returns:
        int: Aire entière du trapèze calculée selon la formule : ((a + b) * h) / 2.
    """
    # Calcul de la somme des bases
    base_sum = a + b
    # Calcul de l'aire en utilisant la formule du trapèze
    area = (base_sum * h) / 2
    # Conversion de l'aire en entier (tronquée)
    return int(area)

def main():
    """
    Fonction principale qui exécute la lecture des entrées, le calcul et l'affichage du résultat.
    """
    # Lire les valeurs d'entrée de l'utilisateur
    a, b, h = read_input()
    # Calculer l'aire du trapèze avec les valeurs saisies
    area = trapezoid_area(a, b, h)
    # Afficher l'aire calculée
    print(area)

# Exécuter la fonction principale
main()
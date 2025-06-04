def convert_to_balanced_ternary(w):
    """
    Convertit un entier en sa représentation à base 3 équilibrée personnalisée.

    Cette fonction prend un entier `w` et produit une chaîne résultant d’un algorithme
    utilisant les caractères '0', '+', et '-' pour représenter les chiffres d’un système
    basé sur une modification de la numération ternaire.

    Args:
        w (int): L'entier à convertir.

    Returns:
        str: La représentation sous forme de chaîne, renversée à la fin, du nombre
        dans le système personnalisé.
    """
    result = ''  # Chaîne pour construire la représentation personnalisée
    chars = '0+-'  # Ensemble des caractères servant à représenter chaque chiffre possible
    n = 0  # Puissance courante de 3

    # Boucle tant que 'w' n'est pas totalement représenté par la partie déjà traitée
    while w > (3 ** n - 1) // 2:
        # Calcule un chiffre à partir de la formule fournie,
        # où (w + (3 ** n - 1) // 2) // (3 ** n) prélève le n-ième chiffre dans la numération,
        # et % 3 le ramène dans l'ensemble {0,1,2} pour l'indexation dans 'chars'.
        index = ((w + (3 ** n - 1) // 2) // (3 ** n)) % 3
        result += chars[index]
        n += 1  # Passe à la puissance suivante

    # Renvoie la chaîne inversée pour remettre les chiffres du poids fort au poids faible
    return result[::-1]

if __name__ == "__main__":
    # Demande un entier à l’utilisateur
    w = int(input())
    # Affiche la représentation personnalisée du nombre fourni
    print(convert_to_balanced_ternary(w))
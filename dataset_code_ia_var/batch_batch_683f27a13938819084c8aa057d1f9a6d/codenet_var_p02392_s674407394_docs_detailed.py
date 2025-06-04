def check_increasing_order(a: int, b: int, c: int) -> bool:
    """
    Vérifie si les trois entiers sont strictement croissants.

    Args:
        a (int): Le premier entier.
        b (int): Le deuxième entier.
        c (int): Le troisième entier.

    Returns:
        bool: True si a < b < c, sinon False.
    """
    # On vérifie si a est strictement inférieur à b, et b est strictement inférieur à c
    return a < b and b < c

def main():
    """
    Lit trois entiers saisis par l'utilisateur, vérifie s'ils sont dans l'ordre croissant strict,
    et affiche 'Yes' ou 'No' selon le résultat.
    """
    # Lecture de la ligne d'entrée, séparation des valeurs, conversion en entiers
    a, b, c = map(int, input().split(' '))
    
    # Appel de la fonction de vérification et affichage du résultat approprié
    if check_increasing_order(a, b, c):
        print('Yes')
    else:
        print('No')

# Point d'entrée du programme
if __name__ == "__main__":
    main()
def check_order(a: int, b: int, c: int) -> str:
    """
    Vérifie si les trois entiers sont strictement croissants.

    Args:
        a (int): Le premier entier.
        b (int): Le deuxième entier.
        c (int): Le troisième entier.

    Returns:
        str: 'Yes' si a < b < c, sinon 'No'.
    """
    # On vérifie si a < b et b < c simultanément.
    if a < b and b < c:
        return 'Yes'
    else:
        return 'No'

def main():
    """
    Lit trois entiers en une seule entrée séparés par des espaces, 
    vérifie s'ils sont strictement croissants et affiche le résultat.
    """
    # Lecture de l'entrée utilisateur ; on récupère trois entiers.
    a, b, c = map(int, input().split())
    # Vérification de l'ordre et affichage du résultat.
    print(check_order(a, b, c))

# Point d'entrée du script
if __name__ == "__main__":
    main()
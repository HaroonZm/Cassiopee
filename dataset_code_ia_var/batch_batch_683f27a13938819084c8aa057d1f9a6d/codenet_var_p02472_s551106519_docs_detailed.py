def read_input():
    """
    Lit une ligne de l'entrée standard et extrait deux entiers.
    
    Returns:
        tuple: Un couple (m, n) d'entiers extraits de l'entrée utilisateur.
    
    Exemple :
        >>> # Si l'utilisateur saisit '3 7'
        >>> read_input()
        (3, 7)
    """
    # Lire une ligne de l'entrée standard, la séparer en éléments, convertir en entiers et les assigner à m et n.
    m, n = map(int, input().split())
    return m, n

def print_sum(m, n):
    """
    Calcule la somme de deux entiers et l'affiche.
    
    Args:
        m (int): Le premier entier à additionner.
        n (int): Le second entier à additionner.
    
    Effet de bord:
        Affiche le résultat de l'addition de m et n.
    
    Exemple :
        >>> print_sum(2, 5)
        7
    """
    # Calculer et afficher la somme de m et n.
    print(m + n)

if __name__ == "__main__":
    # Lire les deux entiers de l'utilisateur
    m, n = read_input()
    # Calculer et afficher la somme
    print_sum(m, n)
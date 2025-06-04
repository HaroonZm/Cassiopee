def read_integer():
    """
    Lit un entier à partir de l'entrée standard (clavier).
    
    Returns:
        int: L'entier saisi par l'utilisateur.
    """
    return int(input())

def read_integer_list():
    """
    Lit une ligne depuis l'entrée standard, divise la ligne en éléments,
    convertit chaque élément en entier et retourne la liste résultante.
    
    Returns:
        list of int: Liste des entiers lus depuis l'entrée standard.
    """
    return [int(i) for i in input().split()]

def main():
    """
    Fonction principale du programme :
    - Lit la taille de la liste d'entiers.
    - Lit la liste d'entiers elle-même.
    - Calcule et affiche le minimum, le maximum et la somme de la liste.
    """
    # Lecture du nombre d'éléments (non utilisé ensuite)
    n = read_integer()
    
    # Lecture de la liste des entiers
    data = read_integer_list()
    
    # Calcul et affichage du minimum, du maximum et de la somme de la liste
    print(min(data), max(data), sum(data))

if __name__ == '__main__':
    main()
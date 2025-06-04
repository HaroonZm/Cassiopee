def read_integer_list(prompt=""):
    """
    Lit une liste d'entiers à partir de l'entrée standard.
    
    Args:
        prompt (str): Message affiché à l'utilisateur (optionnel).
        
    Returns:
        list: Liste des entiers saisis par l'utilisateur.
    """
    input(prompt)  # On lit et ignore cette ligne (correspond généralement à une taille ou à un séparateur).
    # Lit la ligne suivante, la découpe en éléments, et les convertit en int.
    return list(map(int, input().split()))

def is_subset(list_a, list_b):
    """
    Vérifie si la liste list_b est un sous-ensemble de list_a.
    
    Args:
        list_a (list): Première liste d'entiers (ensemble principal).
        list_b (list): Deuxième liste d'entiers (ensemble potentiel sous-ensemble).
        
    Returns:
        int: 1 si list_b est un sous-ensemble de list_a, 0 sinon.
    """
    # Conversion des deux listes en ensembles pour effectuer la comparaison d'inclusion.
    set_a = set(list_a)
    set_b = set(list_b)
    # L'opérateur <= vérifie si set_b est un sous-ensemble de set_a.
    return 1 if set_b <= set_a else 0

# Lecture des deux listes d'entiers à comparer depuis l'entrée standard.
a = read_integer_list()
b = read_integer_list()

# Vérification et affichage du résultat : 1 si b est inclus dans a, 0 sinon.
print(is_subset(a, b))
def collect_heights(num_heights):
    """
    Demande à l'utilisateur de saisir un nombre donné de valeurs de taille et les retourne dans une liste.

    Args:
        num_heights (int): Le nombre total de tailles à demander à l'utilisateur.

    Returns:
        list: Liste contenant les tailles saisies (sous forme de chaînes de caractères pour le moment).
    """
    heights = []
    for i in range(num_heights):
        # Demande à l'utilisateur une taille et l'ajoute à la liste
        value = input(f"Saisissez la taille numéro {i+1}: ")
        heights.append(value)
    return heights

def convert_heights_to_numbers(heights):
    """
    Convertit toutes les tailles de la liste en entiers.

    Args:
        heights (list): Liste de tailles sous forme de chaînes de caractères.

    Returns:
        list: Nouvelle liste de tailles converties en entiers.
    """
    return [int(h) for h in heights]

def get_largest_values(heights, n):
    """
    Trie une liste de valeurs par ordre décroissant et retourne les n plus grandes.

    Args:
        heights (list): Liste de nombres représentant les tailles.
        n (int): Nombre d'éléments à retourner.

    Returns:
        list: Les n plus grandes tailles, triées du plus grand au plus petit.
    """
    # Trie la liste en ordre décroissant
    sorted_heights = sorted(heights, reverse=True)
    # Retourne les n premiers éléments de la liste triée
    return sorted_heights[:n]

def display_values(values):
    """
    Affiche chaque valeur de la liste sur une ligne séparée.

    Args:
        values (list): Liste des valeurs à afficher.
    """
    for value in values:
        print(value)

def main():
    """
    Fonction principale orchestrant la collecte, le tri et l'affichage des trois plus grandes tailles.
    """
    NUMBER_OF_HEIGHTS = 10  # Nombre de tailles à saisir
    TOP_N = 3               # Nombre de plus grandes tailles à afficher

    # Collecter les tailles auprès de l'utilisateur
    heights_str = collect_heights(NUMBER_OF_HEIGHTS)
    # Convertir les tailles saisies en entiers
    heights = convert_heights_to_numbers(heights_str)
    # Obtenir les trois plus grandes tailles
    largest_heights = get_largest_values(heights, TOP_N)
    # Afficher les trois plus grandes tailles
    display_values(largest_heights)

# Exécution du programme principal
if __name__ == "__main__":
    main()
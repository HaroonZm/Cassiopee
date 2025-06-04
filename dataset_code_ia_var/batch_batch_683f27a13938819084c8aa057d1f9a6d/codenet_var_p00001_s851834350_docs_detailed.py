def collect_inputs(num_inputs):
    """
    Collecte des entrées utilisateur et les stocke dans une liste.

    Args:
        num_inputs (int): Le nombre d'entrées à collecter.

    Returns:
        list: Liste contenant les entrées utilisateur en tant que chaînes de caractères.
    """
    inputs = []
    # Collecte les entrées utilisateur via la fonction input() et les ajoute à la liste
    for _ in range(num_inputs):
        value = input("Entrez une valeur : ")
        inputs.append(value)
    return inputs

def sort_and_reverse(items):
    """
    Trie une liste dans l'ordre croissant puis renverse l'ordre pour obtenir un tri décroissant.

    Args:
        items (list): La liste d'éléments à trier.

    Returns:
        list: Nouvelle liste triée dans l'ordre décroissant.
    """
    # Trie la liste dans l'ordre croissant
    sorted_items = sorted(items)
    # Renverse la liste pour obtenir l'ordre décroissant
    sorted_items.reverse()
    return sorted_items

def print_top_n(items, n):
    """
    Affiche les n premiers éléments d'une liste.

    Args:
        items (list): La liste d'éléments à afficher.
        n (int): Le nombre d'éléments à afficher.
    """
    # Affiche les n premiers éléments de la liste
    for i in range(min(n, len(items))):
        print(items[i])

def main():
    """
    Fonction principale exécutant les étapes du programme :
    1. Collecte 10 entrées utilisateur.
    2. Trie les entrées en ordre décroissant.
    3. Affiche les 3 premières entrées après le tri.
    """
    # Nombre d'entrées utilisateur à collecter
    num_inputs = 10
    # Nombre d'éléments à afficher après le tri
    top_count = 3

    # Collecte les entrées utilisateur
    user_entries = collect_inputs(num_inputs)
    # Trie les entrées en ordre décroissant
    sorted_entries = sort_and_reverse(user_entries)
    # Affiche les 3 premières entrées
    print_top_n(sorted_entries, top_count)

if __name__ == "__main__":
    main()
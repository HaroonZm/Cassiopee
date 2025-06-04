def get_integer_set_from_input(prompt):
    """
    Demande à l'utilisateur d'entrer une liste d'entiers séparés par des espaces,
    puis convertit cette entrée en un ensemble (set) d'entiers.

    Args:
        prompt (str): Le message affiché à l'utilisateur pour saisir les données.

    Returns:
        set: Un ensemble d'entiers résultant de l'entrée utilisateur.
    """
    # Demande une chaîne de caractères à l'utilisateur puis la découpe en éléments
    # Chaque élément est converti en entier et ajouté à un set pour éviter les doublons
    return set(map(int, input(prompt).split()))


def print_sorted_difference(setA, setB):
    """
    Affiche, dans l'ordre croissant, tous les éléments présents dans setA mais pas dans setB.

    Args:
        setA (set): Le premier ensemble d'entiers (dont on veut afficher la différence).
        setB (set): Le second ensemble d'entiers (les éléments à exclure de setA).

    Returns:
        None
    """
    # Calcule la différence entre setA et setB, trie les résultats,
    # puis imprime chaque élément sur une nouvelle ligne
    for elem in sorted(setA.difference(setB)):
        print(elem)


def main():
    """
    Fonction principale du script. Elle gère la saisie des ensembles
    puis affiche la différence triée entre ces ensembles.

    Returns:
        None
    """
    # Lecture et conversion de la taille de l'ensemble A (inutile ici, mais conservé pour compatibilité)
    _ = input("Entrez le nombre d'éléments dans l'ensemble A (inutile, appuyez sur Entrée) : ")
    # Lecture et création de l'ensemble A
    setA = get_integer_set_from_input("Entrez les éléments de l'ensemble A séparés par des espaces : ")

    # Lecture et conversion de la taille de l'ensemble B (inutile ici, mais conservé pour compatibilité)
    _ = input("Entrez le nombre d'éléments dans l'ensemble B (inutile, appuyez sur Entrée) : ")
    # Lecture et création de l'ensemble B
    setB = get_integer_set_from_input("Entrez les éléments de l'ensemble B séparés par des espaces : ")

    # Affiche la différence triée entre setA et setB
    print_sorted_difference(setA, setB)


# Appelle la fonction principale si ce fichier est exécuté comme programme principal
if __name__ == "__main__":
    main()
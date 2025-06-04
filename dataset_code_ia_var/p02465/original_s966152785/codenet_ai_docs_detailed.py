def get_integer_input(prompt):
    """
    Demande à l'utilisateur de saisir un entier, affiche le message donné et retourne l'entier saisi.

    Args:
        prompt (str): Le message à afficher à l'utilisateur lors de la demande de saisie.

    Returns:
        int: L'entier saisi par l'utilisateur.
    """
    return int(input(prompt))


def get_set_of_integers_from_input(prompt):
    """
    Demande à l'utilisateur de saisir une séquence d'entiers séparés par des espaces, 
    puis convertit ces valeurs en un ensemble d'entiers.

    Args:
        prompt (str): Le message à afficher à l'utilisateur lors de la demande de saisie.

    Returns:
        set: Un ensemble d'entiers saisis par l'utilisateur.
    """
    return {int(i) for i in input(prompt).split()}


def compute_sorted_difference_tuple(set1, set2):
    """
    Calcule la différence entre deux ensembles d'entiers, trie les résultats et les retourne sous forme de tuple.

    Args:
        set1 (set): Premier ensemble d'entiers.
        set2 (set): Second ensemble d'entiers à soustraire du premier.

    Returns:
        tuple: Un tuple d'entiers correspondant à la différence triée entre set1 et set2.
    """
    return tuple(sorted(set1 - set2))


def print_tuple_elements(tuple_data):
    """
    Affiche chaque élément du tuple sur une nouvelle ligne.

    Args:
        tuple_data (tuple): Le tuple d'entiers à afficher.
    """
    for item in tuple_data:
        print(item)


def main():
    """
    Fonction principale du programme.
    Gère les entrées utilisateur, le traitement des ensembles, 
    la différence triée, puis l'affichage du résultat.
    """
    # Lire la taille du premier ensemble (peut être utilisé pour vérification mais non utilisé ici)
    n = get_integer_input("")
    
    # Lire le premier ensemble d'entiers depuis l'entrée utilisateur
    a = get_set_of_integers_from_input("")
    
    # Lire la taille du second ensemble (peut être utilisé pour vérification mais non utilisé ici)
    m = get_integer_input("")
    
    # Lire le second ensemble d'entiers depuis l'entrée utilisateur
    b = get_set_of_integers_from_input("")
    
    # Calculer la différence entre les deux ensembles, trier le résultat et le transformer en tuple
    c = compute_sorted_difference_tuple(a, b)
    
    # Afficher chaque élément du tuple résultant sur une ligne séparée
    print_tuple_elements(c)


# Exécution du script principal
if __name__ == "__main__":
    main()
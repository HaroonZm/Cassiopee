def read_integer_list(prompt=""):
    """
    Lit une ligne d'entrée standard, la découpe en éléments séparés par des espaces
    puis convertit chaque élément en un entier.

    Args:
        prompt (str): Message facultatif à afficher avant de lire l'entrée.

    Returns:
        list: Liste des entiers lus depuis l'entrée utilisateur.
    """
    return [int(x) for x in raw_input(prompt).split()]

def main():
    """
    Fonction principale du programme qui lit deux listes d'entiers depuis l'entrée
    utilisateur, puis affiche le nombre d'éléments communs entre les deux listes.
    """
    # Lecture de la première valeur n, généralement la taille de la première liste (peut être ignorée ici)
    n = raw_input("Entrer la taille de la première liste: ")
    
    # Lecture et conversion de la première liste d'entiers
    l1 = read_integer_list("Entrer la première liste d'entiers séparés par des espaces:\n")
    
    # Lecture de la seconde valeur n, généralement la taille de la seconde liste (peut être ignorée ici)
    n = raw_input("Entrer la taille de la seconde liste: ")
    
    # Lecture et conversion de la seconde liste d'entiers
    l2 = read_integer_list("Entrer la seconde liste d'entiers séparés par des espaces:\n")
    
    # Calcul de l'intersection entre les deux ensembles et affichage de la cardinalité
    print len(set(l1) & set(l2))

if __name__ == "__main__":
    main()
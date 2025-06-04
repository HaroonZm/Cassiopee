def read_set_from_input(prompt):
    """
    Lit une ligne d'entrée standard composée d'entiers séparés par des espaces,
    puis retourne un ensemble contenant ces entiers.

    Parameters:
        prompt (str): Texte à afficher pour inviter l'utilisateur à saisir les données.

    Returns:
        set: Ensemble d'entiers saisis par l'utilisateur.
    """
    # Affiche le prompt et lit une ligne, puis convertit chaque nombre en entier et crée un ensemble
    return set(map(int, input(prompt).split()))

def main():
    """
    Cette fonction principale lit deux ensembles d'entiers depuis l'entrée utilisateur,
    puis affiche les éléments qui appartiennent au premier ensemble mais pas au second,
    dans l'ordre croissant.
    """
    # Lecture du nombre d'éléments du premier ensemble (peut être ignoré ensuite)
    n = int(input("Entrez le nombre d'éléments de l'ensemble A : "))
    # Lecture des éléments et création de l'ensemble A
    a = read_set_from_input("Entrez les éléments de l'ensemble A séparés par des espaces : ")
    
    # Lecture du nombre d'éléments du second ensemble (peut être ignoré ensuite)
    m = int(input("Entrez le nombre d'éléments de l'ensemble B : "))
    # Lecture des éléments et création de l'ensemble B
    b = read_set_from_input("Entrez les éléments de l'ensemble B séparés par des espaces : ")
    
    # Calcule la différence des ensembles (éléments dans A mais pas dans B)
    difference = a - b
    # Tri les éléments de la différence dans l'ordre croissant
    for element in sorted(difference):
        print(element)

if __name__ == "__main__":
    main()
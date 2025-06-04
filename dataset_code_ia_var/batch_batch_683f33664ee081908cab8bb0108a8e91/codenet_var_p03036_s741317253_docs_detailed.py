def sequence_calculation(r, D, x):
    """
    Calcule et affiche les 10 premiers termes d'une suite récurrente définie par :
    x_{n+1} = r * x_n - D

    Args:
        r (int): Le multiplicateur appliqué à chaque terme précédent.
        D (int): La constante soustraite à chaque itération.
        x (int): Le terme initial de la suite.

    Returns:
        None: Affiche chaque terme généré à chaque étape.
    """
    # Boucle sur 10 itérations pour calculer et afficher chaque terme de la suite
    for i in range(1, 11):
        # Calcul du nouveau terme selon la relation de récurrence
        x = r * x - D
        # Affichage du terme actuel
        print(x)

if __name__ == "__main__":
    # Lecture des trois entiers r, D, x depuis l'entrée standard
    r, D, x = map(int, input("Entrez r, D et x séparés par des espaces : ").split())
    # Appel de la fonction pour générer et afficher les termes de la suite
    sequence_calculation(r, D, x)
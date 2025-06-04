def recurrence_sequence(r, d, x):
    """
    Calcule et affiche les dix premiers termes d'une suite définie par la récurrence :
    y = r * x - d

    Paramètres :
    r (int) : multiplicateur de la récurrence
    d (int) : valeur à soustraire à chaque itération
    x (int) : valeur initiale de la suite

    Cette fonction affiche chacun des dix termes successifs de la suite.
    """
    for i in range(10):
        # Calcul du nouveau terme selon la formule de récurrence
        y = r * x - d
        # Affichage du terme courant
        print(y)
        # La valeur de x pour l'itération suivante devient la valeur de y courante
        x = y

def main():
    """
    Fonction principale qui lit les entrées de l'utilisateur, puis appelle la fonction
    de calcul de la suite récurrente.

    L'utilisateur doit fournir trois entiers séparés par des espaces : r, d et x.
    """
    # Lecture et conversion des entrées utilisateur (r, d, x)
    r, d, x = map(int, input().split())
    # Appel de la fonction pour afficher la suite
    recurrence_sequence(r, d, x)

# Point d'entrée du programme
if __name__ == "__main__":
    main()
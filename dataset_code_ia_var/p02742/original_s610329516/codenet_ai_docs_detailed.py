def calculate_max_cells(h, w):
    """
    Calcule le nombre maximum de cellules pouvant être sélectionnées dans une grille de dimensions h x w
    sans que deux cellules sélectionnées ne soient adjacentes horizontalement ou verticalement.

    Paramètres:
        h (int): hauteur de la grille (nombre de lignes)
        w (int): largeur de la grille (nombre de colonnes)

    Retourne:
        int: Nombre maximum de cellules sélectionnées sous la contrainte spécifiée.
    """
    # Cas particulier : si l'une des dimensions est 1 (ligne ou colonne unique)
    if w == 1 or h == 1:
        # Dans ce cas, on ne peut sélectionner qu'une seule cellule au maximum
        return 1
    # Cas où le nombre de lignes est pair
    elif h % 2 == 0:
        # On peut sélectionner une cellule sur deux dans chaque ligne
        # On remplit la moitié des lignes (h//2), en prenant toutes les colonnes à chaque fois
        return w * (h // 2)
    else:
        # Pour une hauteur impaire, on prend le maximum dans la "moitié entière" des lignes
        # Pour la ligne supplémentaire, on peut remplir environ la moitié de ses cellules (arrondi supérieur)
        # int(w / 2 + 0.5) permet de faire un arrondi supérieur pour w impair
        return w * (h // 2) + int(w / 2 + 0.5)

if __name__ == "__main__":
    # Lecture des dimensions h et w de la grille depuis l'entrée standard
    h, w = map(int, input().split())

    # Calcul et affichage du résultat
    print(calculate_max_cells(h, w))
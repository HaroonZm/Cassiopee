def is_point_inside_rectangle(coords):
    """
    Détermine si un point est à l'intérieur d'un rectangle ou non, selon les coordonnées fournies.

    Args:
        coords (list of float): Une liste de 8 nombres flottants représentant les coordonnées suivantes :
            [x1, y1, x2, y2, x3, y3, x4, y4], où
            (x1, y1), (x2, y2) sont des points formant un segment de ligne,
            (x3, y3), (x4, y4) sont deux autres points servant pour la comparaison.

    Returns:
        str: 'YES' si le point est dans le rectangle selon la logique, 'NO' sinon.
    """
    # Selon la logique du code initial, on vérifie quatre conditions sur les coordonnées.
    # Si l'une des conditions est satisfaite, le résultat est 'NO', sinon 'YES'.
    if (coords[0] < coords[4] > coords[2] or
        coords[0] > coords[6] < coords[2] or
        coords[1] < coords[5] > coords[3] or
        coords[1] > coords[7] < coords[3]):
        return 'NO'
    else:
        return 'YES'

def main():
    """
    Lit les entrées de l'utilisateur jusqu'à la fin du fichier (EOF), traite chaque ligne,
    et affiche 'YES' ou 'NO' selon que la condition est satisfaite ou non.

    Utilise la fonction is_point_inside_rectangle pour réaliser la vérification.
    """
    try:
        while True:
            # Lire une ligne de l'entrée, la séparer en différentes valeurs flottantes.
            try:
                line = raw_input()  # Utilisation de raw_input pour Python 2.x
            except NameError:
                line = input()      # Compatibilité Python 3.x

            # Convertir la ligne en une liste de flottants.
            values = list(map(float, line.split()))

            # Vérifier et afficher le résultat selon la logique.
            print(is_point_inside_rectangle(values))
    except EOFError:
        # Lorsque l'utilisateur termine la saisie (EOF), arrêter proprement le programme.
        pass

# Lancer le programme principal lorsque ce fichier est exécuté.
if __name__ == '__main__':
    main()
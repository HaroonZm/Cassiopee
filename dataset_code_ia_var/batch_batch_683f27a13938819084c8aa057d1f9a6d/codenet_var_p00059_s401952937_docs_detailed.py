def is_rectangle_inside(ax, ay, bx, by, cx, cy, dx, dy):
    """
    Détermine si le rectangle défini par les sommets (A,B) contient le rectangle défini par les sommets (C,D).

    Args:
        ax, ay (float): Coordonnées du coin inférieur gauche du rectangle 1 (A).
        bx, by (float): Coordonnées du coin supérieur droit du rectangle 1 (B).
        cx, cy (float): Coordonnées du coin inférieur gauche du rectangle 2 (C).
        dx, dy (float): Coordonnées du coin supérieur droit du rectangle 2 (D).

    Returns:
        bool: True si le rectangle 2 est entièrement contenu dans le rectangle 1, False sinon.
    """
    # Vérifie si les coins du deuxième rectangle (C et D) sont bien à l'intérieur du premier rectangle (A et B)
    return (ax <= dx and cx <= bx) and (ay <= dy and cy <= by)

def main():
    """
    Fonction principale qui lit les coordonnées des rectangles, vérifie l'inclusion, et affiche le résultat.
    Elle continue jusqu'à ce qu'aucune entrée valable ne soit fournie.
    """
    while True:
        try:
            # Lecture d'une ligne d'entrée utilisateur et conversion en float
            ax, ay, bx, by, cx, cy, dx, dy = map(float, input().split())
        except:
            # Si une exception survient (fin d'entrée ou format incorrect), terminer la boucle
            break

        # Appel de la fonction pour vérifier si le deuxième rectangle est inclus dans le premier
        if is_rectangle_inside(ax, ay, bx, by, cx, cy, dx, dy):
            print('YES')
        else:
            print('NO')

# Démarrage du programme principal
if __name__ == "__main__":
    main()
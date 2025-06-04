def draw_rectangle(H, W):
    """
    Dessine un rectangle d'hauteur H et de largeur W. 
    Les bordures du rectangle sont composées de '#', 
    tandis que l'intérieur est rempli de '.'.

    Args:
        H (int): Hauteur du rectangle (nombre de lignes).
        W (int): Largeur du rectangle (nombre de colonnes).
    """
    for i in range(H):
        # Parcourt chaque ligne du rectangle
        for j in range(W):
            # Parcourt chaque colonne de la ligne courante
            # Les caractères des bords sont '#'
            if i == 0 or i == H - 1 or j == 0 or j == W - 1:
                print("#", end="")
            else:
                # Les autres caractères à l'intérieur sont '.'
                print(".", end="")
        # Nouvelle ligne après chaque rangée
        print()
    # Ligne vide après chaque rectangle pour la séparation
    print()

def main():
    """
    Boucle principale pour lire les entrées de l'utilisateur,
    dessiner les rectangles spécifiés, et arrêter lorsque l'entrée est (0, 0).
    """
    while True:
        # Lecture des dimensions (H, W) à partir de l'entrée utilisateur
        H, W = map(int, input().split())
        # Condition d'arrêt : si H et W valent tous les deux 0
        if H == 0 and W == 0:
            break
        # Dessine le rectangle avec la hauteur et la largeur données
        draw_rectangle(H, W)

if __name__ == "__main__":
    # Point d'entrée du programme
    main()
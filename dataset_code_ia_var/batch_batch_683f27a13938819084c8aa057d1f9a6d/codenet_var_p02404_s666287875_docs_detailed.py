def draw_rectangle(height, width):
    """
    Génère une chaîne représentant un rectangle de hauteur `height` et de largeur `width`.
    Les bords du rectangle sont faits de caractères '#', l'intérieur est rempli de '.' sauf
    pour les deux premières et les deux dernières lignes, qui sont totalement composées de '#'.

    Args:
        height (int): Hauteur du rectangle (nombre de lignes)
        width (int): Largeur du rectangle (nombre de colonnes)

    Returns:
        str: Chaîne de caractères représentant le rectangle, terminée par un saut de ligne.
    """
    # Crée la ligne supérieure du rectangle, composée uniquement de '#'
    top_line = '#' * width + '\n'

    # Crée la ligne inférieure du rectangle, identique à la ligne supérieure
    bottom_line = '#' * width + '\n'

    # Si la hauteur est supérieure à 2, il y a des lignes intermédiaires à générer
    if height > 2:
        # Chaque ligne intermédiaire commence et finit par '#' et contient des '.' à l'intérieur
        middle_line = '#' + '.' * (width - 2) + '#' + '\n'
        # On répète la ligne intermédiaire pour chaque ligne entre la première et la dernière
        rectangle = top_line + middle_line * (height - 2) + bottom_line
    # Si la hauteur est exactement 2, il n'y a que la première et la dernière ligne
    elif height == 2:
        rectangle = top_line + bottom_line
    # Si la hauteur est 1, le rectangle est réduit à une seule ligne
    else:
        rectangle = top_line
    return rectangle

def main():
    """
    Fonction principale qui lit les entrées de l'utilisateur, construit les rectangles demandés
    et les affiche jusqu'à ce que '0 0' soit saisi.
    """
    while True:
        # Lit et analyse la ligne entrée par l'utilisateur (fonctionne en Python 2)
        H, W = map(int, raw_input().split())
        
        # Si H et W valent tous les deux 0, on termine la boucle
        if H == 0 and W == 0:
            break
        
        # Affiche le rectangle généré pour les dimensions demandées
        print(draw_rectangle(H, W))

# Point d'entrée du script
if __name__ == '__main__':
    main()
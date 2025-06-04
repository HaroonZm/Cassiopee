import math

def calculate_tiles(w, h, c):
    """
    Calcule le nombre total de tuiles nécessaires pour couvrir une zone de dimensions w x h avec un tuilage c. 
    La fonction réduit d'abord les dimensions à leur plus petit ratio possible en utilisant le PGCD, puis
    multiplie le résultat simplifié par le nombre de couches/tuilages c.

    Args:
        w (int): Largeur de la zone à couvrir.
        h (int): Hauteur de la zone à couvrir.
        c (int): Facteur de tuilage (nombre de fois où la zone est couverte).

    Returns:
        int: Nombre total de tuiles nécessaires.
    """
    # Calcul du Plus Grand Commun Diviseur (PGCD) entre la largeur et la hauteur
    g = math.gcd(w, h)
    # On décompose la surface en rectangles élémentaires sans redondance
    nb_rectangles = (w / g) * (h / g)
    # On multiplie par le facteur de tuilage
    total_tiles = int(nb_rectangles * c)
    return total_tiles

def main():
    """
    Fonction principale qui lit les entrées utilisateur, exécute le calcul
    et affiche le résultat.
    """
    # Lecture des dimensions de la zone et du facteur de tuilage depuis l'entrée standard
    w, h, c = map(int, input().split())
    # Appel de la fonction de calcul et affichage du résultat
    print(calculate_tiles(w, h, c))

# Appel point d'entrée du script
if __name__ == "__main__":
    main()
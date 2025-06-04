import math

def calculate_sphere_volume(radius):
    """
    Calcule le volume d'une sphère en fonction de son rayon.
    
    Paramètres :
        radius (float) : Le rayon de la sphère.
    
    Retourne :
        float : Le volume de la sphère.
    """
    # Calcul du volume d'une sphère avec la formule V = (4/3) * π * r^3
    volume = (4 / 3) * math.pi * (radius ** 3)
    return volume

def main():
    """
    Fonction principale qui lit deux entiers à partir de l'entrée standard,
    extrait le second comme rayon, puis calcule et affiche le volume de la sphère.
    """
    # Lecture de deux entiers depuis l'entrée, séparés par un espace
    a, b = map(int, input().split())
    # Calcul du volume de la sphère de rayon 'b'
    sphere_volume = calculate_sphere_volume(b)
    # Affichage du résultat
    print(sphere_volume)

# Point d'entrée du programme
if __name__ == "__main__":
    main()
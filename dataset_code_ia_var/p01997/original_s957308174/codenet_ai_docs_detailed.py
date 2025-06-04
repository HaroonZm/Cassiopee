import math

def calculate_sphere_volume(radius):
    """
    Calcule le volume d'une sphère à partir de son rayon.

    Args:
        radius (float): Le rayon de la sphère.

    Returns:
        float: Le volume de la sphère.
    """
    # Calcul du volume en utilisant la formule (4/3) * π * r^3
    volume = (4.0 / 3.0) * math.pi * (radius ** 3)
    return volume

def main():
    """
    Point d'entrée du programme.
    Demande à l'utilisateur d'entrer deux entiers séparés par un espace,
    puis calcule et affiche le volume d'une sphère en utilisant la deuxième valeur.
    """
    # Demande à l'utilisateur de saisir deux entiers séparés par un espace
    # Par exemple, '3 5' où le premier nombre est ignoré
    a, b = map(int, input("Entrez deux entiers séparés par un espace : ").split())
    
    # Conversion de 'b' en flottant pour une précision accrue lors du calcul
    radius = float(b)
    
    # Calcul du volume de la sphère avec le rayon 'b'
    volume = calculate_sphere_volume(radius)
    
    # Affichage du résultat
    print(volume)

# Exécute la fonction principale si ce script est exécuté directement
if __name__ == "__main__":
    main()
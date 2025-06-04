from math import pi

def calculate_sphere_volume(radius):
    """
    Calcule le volume d'une sphère à partir de son rayon.

    Args:
        radius (float): Le rayon de la sphère.

    Returns:
        float: Le volume de la sphère.
    """
    # Formellement, le volume d'une sphère = (4/3)*pi*rayon^3
    return (4/3) * pi * (radius ** 3)

def main():
    """
    Point d'entrée principal du programme.
    Lit deux valeurs flottantes, calcule et affiche le volume de la sphère
    dont le rayon correspond à la seconde valeur lue.
    """
    # Lecture d'une ligne d'entrée et conversion en deux flottants.
    # La première valeur est stockée dans A (non utilisée ici), la seconde dans B.
    A, B = map(float, input().split())
    # Calcul du volume de la sphère de rayon B.
    volume = calculate_sphere_volume(B)
    # Affichage du résultat avec une précision de 10 chiffres après la virgule.
    print('{:.10f}'.format(volume))

# Exécution de la fonction principale lorsque le script est lancé
if __name__ == "__main__":
    main()
import math

def calculer_volume_sphere(rayon):
    """
    Calcule le volume d'une sphère à partir de son rayon.

    Paramètres:
        rayon (float): Le rayon de la sphère.

    Retourne:
        float: Le volume de la sphère.
    """
    # Calcule le volume en utilisant la formule (4/3) * pi * r^3
    volume = (4/3) * math.pi * rayon ** 3
    return volume

def main():
    """
    Fonction principale exécutant l'entrée des données, l'appel à la fonction de calcul,
    et l'affichage du résultat.
    """
    # Demande à l'utilisateur de saisir deux entiers séparés par un espace
    # On utilise uniquement le second entier saisi (b), en ignorant le premier (a)
    a, b = map(int, input("Entrez deux entiers séparés par un espace : ").split())

    # Calcule le volume de la sphère de rayon b
    volume = calculer_volume_sphere(b)

    # Affiche le résultat du calcul
    print(volume)

if __name__ == "__main__":
    # Point d'entrée du programme
    main()
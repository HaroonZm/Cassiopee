import sys

def read_integer_from_stdin():
    """
    Lit une ligne depuis l'entrée standard et retourne sa valeur entière.

    Returns:
        int: L'entier lu depuis l'entrée standard.
    """
    return int(sys.stdin.readline())

def sum_times(a, b, c, d):
    """
    Calcule la somme de quatre nombres entiers représentant des secondes,
    puis convertit la somme totale en minutes et secondes séparément.

    Args:
        a (int): Premier entier représentant des secondes.
        b (int): Deuxième entier représentant des secondes.
        c (int): Troisième entier représentant des secondes.
        d (int): Quatrième entier représentant des secondes.

    Returns:
        tuple: Un tuple contenant deux éléments :
            - int: Le nombre total de minutes.
            - int: Le nombre restant de secondes après conversion en minutes.
    """
    total_seconds = a + b + c + d  # Somme des quatre entrées
    minutes = total_seconds // 60   # Nombre entier de minutes
    seconds = total_seconds % 60    # Secondes restantes après conversion
    return minutes, seconds

def main():
    """
    Fonction principale du programme :
    Lit quatre entiers depuis l'entrée standard, calcule la somme totale,
    puis affiche le nombre de minutes et de secondes résultant.
    """
    # Lecture des quatre entiers représentant des secondes
    a = read_integer_from_stdin()
    b = read_integer_from_stdin()
    c = read_integer_from_stdin()
    d = read_integer_from_stdin()

    # Calcul de la conversion en minutes et secondes
    minutes, seconds = sum_times(a, b, c, d)

    # Affichage du résultat
    print(minutes)
    print(seconds)

# Point d'entrée du script
if __name__ == "__main__":
    main()
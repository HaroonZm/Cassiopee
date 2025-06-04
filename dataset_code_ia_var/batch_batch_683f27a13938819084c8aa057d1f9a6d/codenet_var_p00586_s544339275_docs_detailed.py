import sys

def process_input_line(line):
    """
    Prend une ligne d'entrée, extrait deux entiers séparés par des espaces,
    et retourne leur somme.

    Args:
        line (str): Une chaîne de caractères contenant deux entiers séparés par des espaces.

    Returns:
        int: La somme des deux entiers extraits de la ligne.
    """
    # Découpe la ligne sur les espaces et convertit les deux parties en entiers
    a, b = [int(x) for x in line.split()]
    # Calcule la somme des deux entiers
    return a + b

def main():
    """
    Lit les lignes de l'entrée standard, calcule et affiche la somme pour chaque paire d'entiers.
    """
    # Parcours chaque ligne reçue sur l'entrée standard (typiquement la saisie ou un fichier redirigé)
    for line in sys.stdin:
        # Traite la ligne pour obtenir la somme de deux entiers
        result = process_input_line(line)
        # Affiche le résultat
        print(result)

if __name__ == "__main__":
    # Point d'entrée principal du programme
    main()
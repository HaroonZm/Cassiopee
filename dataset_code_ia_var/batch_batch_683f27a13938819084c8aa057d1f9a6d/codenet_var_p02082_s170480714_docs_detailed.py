def read_integers():
    """
    Lit deux entiers séparés par un espace sur une seule ligne de l'entrée standard.

    Returns:
        tuple: Un tuple contenant deux entiers (s, t).
    """
    # Demande à l'utilisateur de saisir deux entiers séparés par un espace
    s, t = map(int, input().split())
    return s, t

def skip_line():
    """
    Ignore une ligne d'entrée standard.
    Utilisée ici pour ignorer une ligne spécifique de l'entrée.
    """
    # Lecture et rejet d'une ligne, utilisée pour ignorer une entrée inutile
    input()

def read_integer():
    """
    Lit un entier depuis l'entrée standard.

    Returns:
        int: L'entier lu depuis l'entrée.
    """
    # Demande à l'utilisateur de saisir un entier et le renvoie
    return int(input())

def main():
    """
    Fonction principale orchestrant la lecture des entrées et l'affichage du résultat.

    - Lit deux entiers, s et t, depuis l'entrée standard.
    - Ignore la seconde ligne de l'entrée.
    - Lit un troisième entier depuis l'entrée.
    - Calcule le résultat de l'opération XOR : s ^ t ^ u.
    - Affiche le résultat obtenu.
    """
    # Lecture des deux premiers entiers
    s, t = read_integers()
    # Ignore la deuxième ligne de l'entrée
    skip_line()
    # Lecture du troisième entier
    u = read_integer()
    # Effectue l'opération XOR sur les trois entiers et affiche le résultat
    print(s ^ t ^ u)

if __name__ == "__main__":
    main()
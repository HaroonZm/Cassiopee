def find_first_double_x_or_N(N: int, s: str) -> int:
    """
    Recherche la première occurrence du motif 'xx' dans la chaîne s.
    Si le motif est trouvé, retourne la position (1-indexée) du début du motif.
    Sinon, retourne la valeur N fournie.

    Arguments:
    N -- entier retourné si 'xx' n'est pas trouvé.
    s -- chaîne à analyser.

    Retourne :
    int -- position 1-idxée de 'xx' ou N.
    """
    try:
        # Cherche l'index de la première occurrence de 'xx'
        index = s.index("xx")
        # Retourne l'index + 1 car on veut une position 1-indexée
        return index + 1
    except ValueError:
        # Si 'xx' n'est pas trouvé, retourne N
        return N

def main():
    """
    Fonction principale : lit l'entrée, exécute la recherche, affiche le résultat.
    """
    # Lecture de l'entier N depuis l'entrée standard
    N = int(input())
    # Lecture de la chaîne de caractères à analyser
    s = input()
    # Recherche de 'xx' ou retourne N, puis affiche le résultat
    print(find_first_double_x_or_N(N, s))

# Appel du point d'entrée principal
main()
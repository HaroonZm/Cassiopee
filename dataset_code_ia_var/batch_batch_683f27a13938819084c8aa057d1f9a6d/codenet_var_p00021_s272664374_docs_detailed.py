import sys

def read_input():
    """
    Lit toutes les lignes depuis l'entrée standard (stdin) et les retourne sous forme de liste de chaînes de caractères.
    """
    return sys.stdin.readlines()

def preprocess_lines(input_lines):
    """
    Traite chaque ligne en supprimant le caractère de fin de ligne puis en divisant chaque ligne en une liste d'éléments.

    Args:
        input_lines (list of str): Liste des lignes d'entrée.

    Returns:
        list: liste où chaque élément est une liste de chaînes correspondant à une ligne découpée.
    """
    stripped_lines = [line.rstrip('\n') for line in input_lines]
    split_lines = [line.split(" ") for line in stripped_lines]
    return split_lines

def are_segments_parallel(coords):
    """
    Détermine si deux segments définis par quatre points sont parallèles.

    Args:
        coords (list of str or float): Une liste contenant 8 nombres correspondant aux coordonnées x1, y1, x2, y2, x3, y3, x4, y4.

    Returns:
        bool: True si les deux segments sont parallèles, False sinon.
    """
    # Conversion des coordonnées en float si ce n'est pas déjà fait
    x1, y1, x2, y2, x3, y3, x4, y4 = map(float, coords)
    # Calcul des vecteurs directeurs des deux segments
    X1 = x2 - x1
    Y1 = y2 - y1
    X2 = x4 - x3
    Y2 = y4 - y3
    # Vérification du parallélisme via le déterminant (produit croisé)
    return abs(X1 * Y2 - X2 * Y1) < 1e-10

def process_segments():
    """
    Fonction principale : lit les segments depuis stdin, détermine pour chaque paire de segments s'ils sont parallèles
    et affiche "YES" si c'est le cas ou "NO" sinon.
    """
    input_lines = read_input()
    split_lines = preprocess_lines(input_lines)

    # La première ligne contient le nombre de cas à traiter
    n = int(split_lines[0][0])
    # Suppression de l'en-tête contenant n
    split_lines.pop(0)

    # Pour chaque segment, vérifie le parallélisme et affiche le résultat
    for coords in split_lines:
        if are_segments_parallel(coords):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    process_segments()
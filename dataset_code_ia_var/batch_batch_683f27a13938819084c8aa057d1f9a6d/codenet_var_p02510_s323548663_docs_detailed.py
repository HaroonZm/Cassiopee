def read_string():
    """
    Lit une chaîne de caractères depuis l'entrée standard.
    Retourne :
        str : la chaîne entrée par l'utilisateur.
    """
    return raw_input()

def read_integer():
    """
    Lit un entier depuis l'entrée standard et le retourne.
    Retourne :
        int : l'entier entré par l'utilisateur.
    """
    return int(raw_input())

def calculate_total_rotation(num_operations):
    """
    Calcule la somme des décalages à effectuer sur la chaîne.
    Args:
        num_operations (int): Nombre de décalages à effectuer.
    Retourne :
        int : somme totale des décalages.
    """
    total = 0
    for _ in range(num_operations):
        amount = read_integer()
        total += amount
    return total

def rotate_string(s, rotation_amount):
    """
    Effectue une rotation circulaire vers la gauche sur une chaîne.
    Args:
        s (str): La chaîne à faire tourner.
        rotation_amount (int): Le nombre de caractères à décaler.
    Retourne :
        str : la chaîne après rotation circulaire.
    """
    n = len(s)
    rotation = rotation_amount % n  # S'assure que rotation < longueur de s
    return s[rotation:] + s[:rotation]

def main_loop():
    """
    Boucle principale du programme :
    - Lis une chaîne de caractères.
    - Si la chaîne est "-", le programme se termine.
    - Sinon, lit un nombre d'opérations, puis les décalages successifs.
    - Applique la rotation finale à la chaîne et l'affiche.
    """
    while True:
        ls = read_string()
        if ls == "-":
            break  # Sortie de la boucle si l'utilisateur entre "-"
        h = 0  # Stocke la somme totale des décalages demandés
        num_ops = read_integer()  # Nombre de décalages à effectuer
        h = calculate_total_rotation(num_ops)
        rotated = rotate_string(ls, h)
        print rotated

# Lancement du programme
main_loop()
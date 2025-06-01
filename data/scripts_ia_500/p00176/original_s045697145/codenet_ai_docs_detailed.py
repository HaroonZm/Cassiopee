import math

# Liste des couleurs prédéfinies avec leurs noms et valeurs RGB associées
L = [
    ("black", 0, 0, 0),
    ("blue", 0, 0, 255),
    ("lime", 0, 255, 0),
    ("aqua", 0, 255, 255),
    ("red", 255, 0, 0),
    ("fuchsia", 255, 0, 255),
    ("yellow", 255, 255, 0),
    ("white", 255, 255, 255)
]

def hex_to_rgb(hex_color):
    """
    Convertit une chaîne de caractères représentant une couleur hexadécimale en tuple RGB.

    Args:
        hex_color (str): Une chaîne de la forme '#RRGGBB'.

    Returns:
        tuple: Un tuple (R, G, B) où R, G et B sont des entiers entre 0 et 255.
    """
    # Extraction des composantes rouges, vertes et bleues depuis la chaîne hexadécimale
    R = int(hex_color[1:3], 16)
    G = int(hex_color[3:5], 16)
    B = int(hex_color[5:7], 16)
    return R, G, B

def distance_rgb(c1, c2):
    """
    Calcule la distance euclidienne entre deux couleurs en espace RGB.

    Args:
        c1 (tuple): Première couleur sous forme de tuple (R, G, B).
        c2 (tuple): Deuxième couleur sous forme de tuple (R, G, B).

    Returns:
        float: La distance euclidienne entre c1 et c2.
    """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2 + (c1[2] - c2[2])**2)

def couleur_plus_proche(hex_color, couleurs):
    """
    Trouve la couleur la plus proche parmi une liste de couleurs prédéfinies 
    par rapport à une couleur donnée en hexadécimal.

    Args:
        hex_color (str): Couleur au format hexadécimal '#RRGGBB'.
        couleurs (list): Liste de tuples (nom_couleur, R, G, B).

    Returns:
        str: Le nom de la couleur la plus proche.
    """
    # Conversion de la couleur entrée en RGB
    rgb_input = hex_to_rgb(hex_color)
    min_distance = float('inf')  # Initialiser à une très grande valeur
    couleur_min = None

    # Parcours de toutes les couleurs pour trouver celle la plus proche
    for nom, r, g, b in couleurs:
        dist = distance_rgb((r, g, b), rgb_input)
        if dist < min_distance:
            min_distance = dist
            couleur_min = nom

    return couleur_min

# Boucle principale pour lire des entrées utilisateur et afficher la couleur la plus proche
while True:
    c = raw_input()  # Lecture d'une chaîne hexadécimale
    if c == "0":
        break  # Fin de la boucle si l'entrée est '0'
    # Affichage du nom de la couleur la plus proche dans la liste
    print couleur_plus_proche(c, L)
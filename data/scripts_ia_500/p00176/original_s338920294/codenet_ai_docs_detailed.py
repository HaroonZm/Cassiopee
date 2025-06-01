import math

def hex_to_rgb(hex_color):
    """
    Convertit une couleur hexadécimale au format '#RRGGBB' en une liste RGB.

    Args:
        hex_color (str): Une chaîne de caractères représentant une couleur hexadécimale,
                         commençant par '#' et suivie de 6 caractères hexadécimaux.

    Returns:
        list: Une liste de trois entiers [R, G, B], chaque composante variant de 0 à 255.
    """
    # Extraction et conversion des composantes rouges, vertes et bleues
    red = int(hex_color[1:3], 16)
    green = int(hex_color[3:5], 16)
    blue = int(hex_color[5:7], 16)
    return [red, green, blue]


def closest_basic_color(input_rgb, basic_colors):
    """
    Trouve la couleur de la liste basic_colors la plus proche de la couleur input_rgb,
    en calculant la distance euclidienne dans l'espace RGB.

    Args:
        input_rgb (list): Liste de trois entiers [R, G, B] de la couleur d'entrée.
        basic_colors (list): Liste de listes RGB représentant les couleurs de référence.

    Returns:
        int: L'indice de la couleur la plus proche dans basic_colors.
    """
    min_distance = float('inf')  # Initialisation avec une grande valeur
    closest_index = -1

    # Parcours de chaque couleur de référence
    for i, (r, g, b) in enumerate(basic_colors):
        # Calcul de la distance euclidienne entre la couleur d'entrée et la couleur i
        distance = math.sqrt((r - input_rgb[0]) ** 2 + (g - input_rgb[1]) ** 2 + (b - input_rgb[2]) ** 2)
        # Mise à jour si on trouve une distance plus petite
        if distance < min_distance:
            min_distance = distance
            closest_index = i

    return closest_index


def main():
    """
    Programme principal qui lit des couleurs hexadécimales depuis l'entrée standard,
    détermine et affiche la couleur basique la plus proche parmi une liste prédéfinie,
    jusqu'à ce que l'utilisateur entre '0' pour arrêter.
    """
    # Liste des couleurs de base en RGB
    basic_colors = [
        [0, 0, 0],       # noir
        [0, 0, 255],     # bleu
        [0, 255, 0],     # vert lime
        [0, 255, 255],   # aqua
        [255, 0, 0],     # rouge
        [255, 0, 255],   # fuchsia
        [255, 255, 0],   # jaune
        [255, 255, 255]  # blanc
    ]

    # Correspondance des indices de base_colors vers leurs noms
    color_names = [
        "black",
        "blue",
        "lime",
        "aqua",
        "red",
        "fuchsia",
        "yellow",
        "white"
    ]

    while True:
        # Lecture d'une couleur hexadécimale depuis l'entrée utilisateur
        color_16 = input()
        # Condition d'arrêt du programme
        if color_16 == "0":
            break

        # Conversion de la couleur hexadécimale en RGB
        input_rgb = hex_to_rgb(color_16)

        # Recherche de la couleur de base la plus proche
        closest_index = closest_basic_color(input_rgb, basic_colors)

        # Affichage du nom de la couleur correspondante
        print(color_names[closest_index])


if __name__ == "__main__":
    main()
# Dictionnaire associant des codes hexadécimaux RGB simplifiés à des noms de couleur en anglais.
COLOR = {
    "000000": "black",
    "0000ff": "blue",
    "00ff00": "lime",
    "00ffff": "aqua",
    "ff0000": "red",
    "ff00ff": "fuchsia",
    "ffff00": "yellow",
    "ffffff": "white"
}

def decode_color_code(s: str) -> str:
    """
    Décode une chaîne hexadécimale représentant une couleur en un nom de couleur simplifié.
    
    La chaîne d'entrée est supposée être une représentation hexadécimale de 3 composantes couleur 
    (RGB) codées sur 2 caractères chacun. La fonction analyse les valeurs des composantes en 
    comparant chaque paire de caractères en hexadécimal à la valeur seuil 127 (en décimal).
    
    Pour chaque composante (rouge, vert, bleu), si sa valeur hexadécimale est inférieure ou égale 
    à 127, elle est mappée à "00", sinon à "ff". Ces trois composantes sont concaténées pour 
    former une nouvelle chaîne hexadécimale simplifiée, qui est utilisée comme clé dans le dictionnaire COLOR 
    pour récupérer le nom de la couleur correspondante.
    
    Args:
        s (str): Chaîne hexadécimale représentant une couleur (au moins 6 caractères).
        
    Returns:
        str: Nom de la couleur correspondante dans le dictionnaire COLOR.
    """
    # Initialisation de la chaîne simplifiée représentant la couleur.
    color = ""
    # Parcours des deuxième et troisième caractères, quatrième et cinquième, sixième et septième (index 1-2, 3-4, 5-6)
    # On compare chaque composante couleur en hexadécimal à 127 (0x7f).
    for first, second in zip(s[1::2], s[2::2]):
        # Conversion de la paire hexadécimale en entier.
        component_value = int(first + second, 16)
        # Si la valeur est <= 127, on associe "00" sinon "ff"
        if component_value <= 127:
            color += "00"
        else:
            color += "ff"
    # Retourne le nom de la couleur correspondant à la chaîne simplifiée.
    return COLOR[color]

def main() -> None:
    """
    Boucle principale qui lit des chaînes de caractères depuis l'entrée standard,
    et affiche le nom de couleur associé à chaque chaîne jusqu'à ce qu'une chaîne
    d'une longueur de 1 caractère soit entrée, ce qui indique l'arrêt.
    """
    while True:
        s = input()
        # Condition de sortie : si la longueur de la chaîne est 1, on termine la boucle.
        if len(s) == 1:
            break
        # Décodage et affichage du nom de couleur.
        print(decode_color_code(s))

if __name__ == "__main__":
    main()
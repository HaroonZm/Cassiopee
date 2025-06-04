import sys

# Dictionnaire de correspondance des chiffres romains à leurs valeurs entières
roman_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman_to_int(roman):
    """
    Convertit un nombre romain sous forme de chaîne de caractères en entier.

    Args:
        roman (str): Le nombre romain à convertir (ex. "XIV").

    Returns:
        int: La valeur entière correspondante.
    
    Le principe consiste à parcourir les chiffres romains de gauche à droite.
    Si la valeur d'un chiffre est inférieure à celle du chiffre suivant, elle est soustraite.
    Sinon, elle est ajoutée.
    """
    # Convertit chaque caractère du nombre romain en sa valeur entière
    values = [roman_map[c] for c in roman.strip()]
    total = 0
    # Parcours des valeurs de gauche à droite
    for i in range(len(values)):
        # Applique la soustraction si la prochaine valeur est plus grande
        if i+1 < len(values) and values[i] < values[i+1]:
            total -= values[i]
        else:
            total += values[i]
    return total

def main():
    """
    Fonction principale :
    Pour chaque ligne lue depuis l'entrée standard, interprète la chaîne comme un nombre romain
    et affiche sa valeur entière.
    """
    for line in sys.stdin:
        result = roman_to_int(line)
        print(result)

if __name__ == "__main__":
    main()
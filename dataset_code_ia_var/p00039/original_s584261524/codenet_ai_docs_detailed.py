import sys

# Dictionnaire de correspondance entre les chiffres romains et leurs valeurs entières
roman_to_int = {
    'I':    1,
    'V':    5,
    'X':    10,
    'L':    50,
    'C':    100,
    'D':    500,
    'M':    1000
}

def roman_string_to_int(roman_str):
    """
    Convertit une chaîne de chiffres romains en son équivalent entier.
    
    Cette fonction parcourt chaque caractère du chiffre romain et applique la logique de soustraction
    lorsque la valeur du symbole courant est inférieure à la suivante.
    
    Args:
        roman_str (str): Une chaîne représentant un nombre en chiffres romains (ex: 'XIV')
    
    Returns:
        int: La valeur entière correspondant au chiffre romain donné.
    """
    # Liste contenant la valeur entière correspondant à chaque lettre de la chaîne
    values = [roman_to_int[c] for c in roman_str.strip()]
    total = 0
    for i in range(len(values)):
        # Si le chiffre courant est inférieur au suivant, il s'agit d'une soustraction
        if (i + 1 < len(values)) and (values[i] < values[i + 1]):
            total -= values[i]
        else:
            # Sinon, on l'ajoute normalement au total
            total += values[i]
    return total

def main():
    """
    Lit chaque ligne de l'entrée standard, convertit le chiffre romain en entier et affiche le résultat.
    """
    for line in sys.stdin:
        # Convertir la ligne en entier et afficher le résultat
        result = roman_string_to_int(line)
        print(result)

if __name__ == "__main__":
    main()
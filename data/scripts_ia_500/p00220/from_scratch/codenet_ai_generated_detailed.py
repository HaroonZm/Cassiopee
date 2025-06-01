# Programme Python pour convertir un nombre réel en représentation binaire sous contraintes

def float_to_binary_limited(num):
    """
    Convertit un nombre réel positif en une chaîne binaire limitée à
    8 bits pour la partie entière et 4 bits pour la partie fractionnaire.
    Si la conversion ne tient pas dans cette limite, retourne "NA".

    Args:
        num (float): Le nombre à convertir, supposé >= 0.

    Returns:
        str: La représentation binaire sous la forme "iiiiiiii.ffff" ou "NA".
    """
    # Séparer partie entière et fractionnaire
    integer_part = int(num)
    fractional_part = num - integer_part

    # Convertir la partie entière en binaire (au plus 8 bits)
    # Si la représentation binaire excède 8 bits, retourner NA
    int_bin = bin(integer_part)[2:]  # Supprime le préfixe '0b'
    if len(int_bin) > 8:
        return "NA"
    # Remplir à gauche avec des 0 pour avoir 8 bits
    int_bin = int_bin.zfill(8)

    # Convertir la partie fractionnaire en binaire 4 bits
    frac_bin = ""
    frac = fractional_part
    for _ in range(4):
        frac *= 2
        bit = int(frac)
        frac_bin += str(bit)
        frac -= bit

    # Vérifier que la valeur fractionnaire est bien représentée sur 4 bits,
    # c'est-à-dire que l'arrondi est exact ou que la précision est suffisante
    # Ici, on considère que si on a une partie fractionnaire non nulle après 4 bits,
    # la conversion est tronquée -> retourner NA
    # On regarde la partie restante après 4 bits
    if frac != 0:
        # Il reste des bits non représentés (inférieurs à 2^-4)
        # Cela veut dire que la conversion n'est pas exacte dans 4 bits fractionnaires
        # Donc retourner NA
        return "NA"

    # Retourner la chaîne au format demandé
    return int_bin + "." + frac_bin


def main():
    import sys

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            value = float(line)
        except ValueError:
            # Ligne non convertible -> ignorer
            continue
        if value < 0:
            # Fin du programme
            break
        # Vérifier que la partie entière ne dépasse pas 8 chiffres décimaux
        # et la partie fractionnaire 4 chiffres décimaux selon l'énoncé
        s = line.split(".")
        integer_decimal_digits = len(s[0].lstrip("0")) if s[0].lstrip("0") != "" else 1
        fractional_decimal_digits = len(s[1]) if len(s) > 1 else 0
        if integer_decimal_digits > 8 or fractional_decimal_digits > 4:
            print("NA")
            continue

        # Conversion vers binaire en vérifiant contraintes de taille binaire
        result = float_to_binary_limited(value)
        print(result)


if __name__ == "__main__":
    main()
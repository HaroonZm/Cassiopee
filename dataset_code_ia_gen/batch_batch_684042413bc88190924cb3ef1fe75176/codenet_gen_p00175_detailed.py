# Programme Python pour convertir des nombres décimaux en base 4 avec gestion d'entrées multiples

def decimal_to_base4(n):
    """
    Convertit un entier décimal n en chaîne représentant sa valeur en base 4.
    Si n est 0, retourne '0'.
    """
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        # On récupère le reste de la division par 4 (chiffre en base 4)
        digits.append(str(n % 4))
        # On divise n pour passer au chiffre significatif supérieur
        n //= 4
    # Comme on a récolté les chiffres du moins significatif au plus significatif,
    # il faut inverser la liste avant de joindre en chaîne.
    digits.reverse()
    return ''.join(digits)


def main():
    import sys
    for line in sys.stdin:
        # On enlève les espaces et saut de lignes
        n_str = line.strip()
        if n_str == '-1':
            # Fin des données
            break
        n = int(n_str)
        # Conversion et sortie
        print(decimal_to_base4(n))


if __name__ == "__main__":
    main()
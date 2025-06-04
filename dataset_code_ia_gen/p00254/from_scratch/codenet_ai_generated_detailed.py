def kaprekar_routine(n_str):
    """
    Fonction qui calcule le nombre d'itérations pour atteindre 6174 à partir du nombre à 4 chiffres n_str
    en appliquant la routine de Kaprekar.
    Si tous les chiffres sont identiques, retourne None indiquant NA.
    """
    # Vérification si tous les chiffres sont identiques -> retourner None
    if len(set(n_str)) == 1:
        return None

    count = 0
    current = n_str

    while current != "6174":
        # Trier les chiffres de current dans l'ordre décroissant (L)
        L = "".join(sorted(current, reverse=True))
        # Trier les chiffres de current dans l'ordre croissant (S)
        S = "".join(sorted(current))
        # Calculer la différence L - S (en nombre entier)
        diff = int(L) - int(S)
        # Former la nouvelle chaîne de 4 chiffres, en ajoutant des zéros à gauche si nécessaire
        current = f"{diff:04d}"
        count += 1

    return count


def main():
    import sys

    for line in sys.stdin:
        n_str = line.strip()
        if n_str == "0000":
            break

        # Si la chaîne est plus courte que 4, on la remplit avec des 0 à gauche (cas prévu)
        n_str = n_str.zfill(4)

        result = kaprekar_routine(n_str)
        if result is None:
            print("NA")
        else:
            print(result)


if __name__ == "__main__":
    main()
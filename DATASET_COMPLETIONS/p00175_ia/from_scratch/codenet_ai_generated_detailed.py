# Fonction pour convertir un nombre décimal en base 4
def decimal_to_base4(n):
    # Cas particulier : si n est 0, on retourne simplement "0"
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        # On récupère le reste de la division par 4 (chiffre base 4)
        remainder = n % 4
        digits.append(str(remainder))
        # On divise n par 4 pour passer à la position supérieure
        n = n // 4
    # Les chiffres ont été récupérés en sens inverse, on inverse la liste avant de créer la chaîne
    digits.reverse()
    return "".join(digits)

def main():
    import sys
    for line in sys.stdin:
        n_str = line.strip()
        # Condition d'arrêt à la lecture de -1
        if n_str == "-1":
            break
        n = int(n_str)
        # Conversion de chaque nombre de la liste d'entrée en base 4
        result = decimal_to_base4(n)
        print(result)

if __name__ == "__main__":
    main()
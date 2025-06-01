import sys

def calculate_sum(d):
    """
    Calcule la somme selon la formule spécifiée : 
    somme de d * x^2 pour x allant de d à (600 - d) inclus, par pas de d.

    Args:
        d (int): L'entier utilisé comme pas et multiplicateur dans la somme.

    Returns:
        int: Le résultat de la somme calculée.
    """
    result = 0
    # On parcourt les valeurs de x de d à 600 - d inclus, avec un pas de d
    for x in range(d, 600 - d + 1, d):
        # On ajoute à result la valeur d * x^2
        result += d * x ** 2
    return result

def main():
    """
    Lit les lignes depuis l'entrée standard, convertit chaque ligne en entier,
    calcule la somme pour chaque entier d, et affiche le résultat.
    """
    # Lecture des lignes à partir de l'entrée standard
    for line in sys.stdin:
        # Conversion de la ligne en entier après suppression des espaces
        d = int(line.strip())
        # Calcul de la somme avec la fonction dédiée
        result = calculate_sum(d)
        # Affichage du résultat
        print(result)

if __name__ == "__main__":
    main()
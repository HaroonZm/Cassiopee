import sys

# Définition des bornes de l'intervalle de calcul
a, b = 0, 600

def f(x):
    """
    Calcule le carré d'un nombre donné.

    Args:
        x (int or float): La valeur d'entrée pour laquelle on souhaite calculer le carré.

    Returns:
        int or float: Le carré de la valeur d'entrée x.
    """
    return x ** 2

if __name__ == '__main__':
    # Parcourt chaque ligne reçue sur l'entrée standard
    for line in sys.stdin:
        # Conversion de la ligne lue en entier, servant de pas d'incrémentation
        d = int(line)

        # Initialisation de la somme à zéro pour chaque nouvelle valeur de d
        sum = 0

        # Parcourt l'intervalle [a, b) avec un pas d'incrémentation d
        for i in range(a, b, d):
            # Ajoute à la somme le produit du pas d par la valeur de f(i)
            sum += d * f(i)

        # Affiche la somme calculée pour cette valeur de d
        print(sum)
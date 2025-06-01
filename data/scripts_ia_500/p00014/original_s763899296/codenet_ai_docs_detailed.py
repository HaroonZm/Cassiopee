import sys

def Integral(x):
    """
    Calcule la valeur de la fonction intégrée en un point donné.

    Args:
        x (float): Le point en lequel évaluer la fonction.

    Returns:
        float: La valeur de la fonction x^2.
    """
    return x**2

def test(d):
    """
    Calcule une approximation de l'intégrale de la fonction x^2 
    entre 0 et 600 en utilisant la méthode des rectangles (somme de Riemann).

    Args:
        d (float): Le pas d'intégration, c'est-à-dire la largeur de chaque rectangle.

    Returns:
        float: La somme des aires des rectangles, approximation de l'intégrale.
    """
    s = 0  # initialisation de la somme des aires
    n = int(600 / d)  # nombre de rectangles pour couvrir l'intervalle [0, 600]
    for i in range(1, n):
        # Calcul de la hauteur du rectangle au point d*i puis multiplication par la largeur d
        s += Integral(d * i) * d
    return s

# Lire les valeurs du pas d'intégration depuis l'entrée standard
for d in sys.stdin:
    d = int(d)  # Conversion de la valeur lue en entier
    print(test(d))  # Calcul et affichage de l'approximation de l'intégrale correspondant au pas d'intégration d
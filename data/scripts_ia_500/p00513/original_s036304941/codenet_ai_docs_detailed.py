def p(x):
    """
    Détermine si un nombre entier x est un nombre premier.

    Un nombre premier est un entier supérieur à 1 qui n'a pas d'autres diviseurs
    que 1 et lui-même.

    Args:
        x (int): Le nombre à tester.

    Returns:
        int: 1 si x est premier, 0 sinon.
    """
    # Si x est pair, il n'est pas premier (sauf 2, mais ici 2 ne sera pas testé car on teste des nombres impairs)
    if x % 2 == 0:
        return 0

    # On teste les diviseurs impairs de 3 à la racine carrée de x (incluse)
    # Seuls ces diviseurs sont nécessaires par propriété des nombres premiers
    limite = int(x ** 0.5) + 1
    for i in range(3, limite, 2):
        # Si i divise x, alors x n'est pas premier
        if x % i == 0:
            return 0

    # Si aucun diviseur n'a été trouvé, x est premier
    return 1


def main():
    """
    Lit deux entiers n et m depuis l'entrée standard, et calcule la somme
    des tests de primalité pour m nombres de la forme 2*n + 1.

    Pour chaque i dans [0, m), calcule le nombre premier correspondant à (2*n + 1)
    et en affiche la somme totale.

    Exemples:
        input:
            2
            3
        output:
            3

    Description détaillée:
        - Lit un entier n.
        - Lit un entier m.
        - Pour m fois, calcule p(2*n+1).
        - Affiche la somme des résultats.
    """
    n = int(input())
    m = int(input())

    # Calculer et afficher la somme de p(2*n+1) répété m fois
    resultat = sum(p(2 * n + 1) for _ in range(m))
    print(resultat)


if __name__ == "__main__":
    main()
def main():
    """
    Exécute le script principal pour lire deux entiers, n et m, puis affiche une séquence selon une logique donnée :
    - Pour chaque indice i variant de 0 à n-1 :
        - Si i est strictement inférieur ou égal à n/2, affiche '0'.
        - Sinon, affiche la valeur de m.
    La séquence résultante est affichée sur une seule ligne, séparant chaque élément par un espace (sans espace final).
    """
    # Demande à l'utilisateur de saisir deux entiers séparés par un espace
    n, m = lire_deux_entiers()
    # Boucle sur chaque position de 0 à n-1
    for i in range(n):
        # Si ce n'est pas le premier élément, afficher un espace avant
        if i > 0:
            print(" ", end="")
        # Si i inférieur ou égal à n/2, afficher '0', sinon 'm'
        if i <= n / 2:
            print("0", end="")
        else:
            print("{}".format(m), end="")
    # Passe à la ligne à la fin de la séquence
    print("")


def lire_deux_entiers():
    """
    Lit une ligne de l'entrée standard, attend deux entiers séparés par des espaces, et retourne ces deux entiers.

    Returns:
        tuple: Un couple (n, m) des deux entiers lus.
    """
    # Lis une ligne sur l'entrée, coupe en parties, convertit chaque partie en int, stocke dans n et m
    return [int(a) for a in input().split()]


if __name__ == "__main__":
    main()